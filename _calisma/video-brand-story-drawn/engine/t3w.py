import sys, time
__file__='/Users/ufo/sickscience-work/brandfilm/render3.py'
exec(open(__file__).read().split("if __name__ == '__main__':")[0])
from PIL import Image
ts=sorted(float(x) for x in sys.argv[1].split(','))
k=0; tt=0.0
while k<len(ts):
    im=frame(tt)
    if tt>=ts[k]-1e-6:
        Image.fromarray(finish(im,tt)).save(f'g_{ts[k]:05.2f}.jpg',quality=88); k+=1
    tt+=1/FPS
