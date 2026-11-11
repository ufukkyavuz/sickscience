import os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
HERE=os.path.dirname(os.path.abspath(__file__))
FONT=os.path.expanduser('~/Library/Fonts/FoundersGrotesk-Bold.otf')
FPS,SECS=30,12
TILES=[140,340,560,760]; W=180; H=250; SIZE=170
def digit(c):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); d.text((W/2,H/2),c,font=ImageFont.truetype(FONT,SIZE),fill=(255,255,255,255),anchor='mm'); return im
GLYPH={str(i):digit(str(i)) for i in range(10)}
def frame(plate,ty,t):
    im=plate.copy(); left=59-int(t); s=f"{0:02d}{left:02d}"; prev=f"{0:02d}{left+1:02d}"; ph=t-int(t)
    for i,x in enumerate(TILES):
        g=GLYPH[s[i]]
        if s[i]!=prev[i] and t>=1 and ph<0.2:
            k=ph/0.2; k=1-(1-k)**3; dy=int((1-k)*-46)
            old=GLYPH[prev[i]].copy(); a=old.getchannel('A').point(lambda v:int(v*(1-k))); old.putalpha(a)
            new=g.copy(); new.putalpha(g.getchannel('A').point(lambda v:int(v*k)))
            im.alpha_composite(old,(x,ty+int(k*46))); im.alpha_composite(new,(x,ty+dy))
        else: im.alpha_composite(g,(x,ty))
    return im.convert('RGB')
def render(name,plate,ty,out):
    pl=Image.open(os.path.join(HERE,plate)).convert('RGBA'); w,h=pl.size
    p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{w}x{h}','-r',str(FPS),'-i','-','-f','lavfi','-i',
      f"aevalsrc='0.35*sin(2*PI*1600*t)*exp(-90*mod(t,1)):s=48000:d={SECS}'",'-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-c:a','aac','-af','loudnorm=I=-20:TP=-2','-shortest',out],stdin=subprocess.PIPE)
    for n in range(FPS*SECS): p.stdin.write(frame(pl,ty,n/FPS).tobytes())
    p.stdin.close(); p.wait()
    print(out,p.returncode)
os.makedirs(os.path.join(HERE,'out'),exist_ok=True)
render('feed','b02_feed.png',240,os.path.join(HERE,'out','Head-to-Toe – Countdown – Feed.mp4'))
render('story','b02_story.png',440,os.path.join(HERE,'out','Head-to-Toe – Countdown – Story.mp4'))
