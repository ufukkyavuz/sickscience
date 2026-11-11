import sys, time
__file__='/Users/ufo/sickscience-work/brandfilm/render3.py'
exec(open(__file__).read().split("if __name__ == '__main__':")[0])
from PIL import Image
for tt in [float(x) for x in sys.argv[1].split(',')]:
    t0=time.time(); im=frame(tt); Image.fromarray(finish(im,tt)).save(f'g_{tt:05.2f}.jpg',quality=88); print(tt, round(time.time()-t0,2))
