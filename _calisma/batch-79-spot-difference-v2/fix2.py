import cv2, numpy as np
S=1696/600
# NW: remove scribbled text on the silver half, keep the black stripe
im=cv2.imread('NW_L.png'); ox,oy=int(80*S),int(280*S)
c=im[oy:oy+622, ox:ox+339].astype(int); lum=c.mean(2)
ys,xs=np.where(lum<70)
sel=((ys>380)&(ys<520))|((ys>120)&(ys<270))
sel&=(xs>90)&(xs<240)
a,b=np.polyfit(ys[sel],xs[sel],1)
Y,X=np.mgrid[0:c.shape[0],0:c.shape[1]]
dist=np.abs(X-(a*Y+b))
box=(Y>315)&(Y<385)&(X>120)&(X<245)
m=((lum<170)&(dist>11)&box).astype(np.uint8)*255
m=cv2.dilate(m,np.ones((5,5),np.uint8))
full=np.zeros(im.shape[:2],np.uint8); full[oy:oy+622,ox:ox+339]=m
im=cv2.inpaint(im,full,7,cv2.INPAINT_TELEA); cv2.imwrite('NW_L.png',im); print('nw scribble px',(m>0).sum(), a,b)
cv2.imwrite('/tmp/claude-501/nw_bot2.png', im[oy:oy+622, ox:ox+339])
# SS: composite the jaw region of the edit onto the left image
L=cv2.imread('SS_L.png').astype(float); R=cv2.imread('SS_Redit.png').astype(float)
x0,y0,x1,y1=[int(v*S) for v in (262,262,425,338)]
mask=np.zeros(L.shape[:2],np.float32); mask[y0:y1,x0:x1]=1
mask=cv2.GaussianBlur(mask,(0,0),12)[...,None]
out=L*(1-mask)+R*mask; cv2.imwrite('SS_R.png',out.astype(np.uint8))
d=np.abs(out-L).max(2); ys,xs=np.where(d>30); print('SS diff bbox',xs.min()/1696,ys.min()/2528,xs.max()/1696,ys.max()/2528)
for k in ['PC','DO']:
  a=cv2.imread(f'{k}_L.png').astype(int); b=cv2.imread(f'{k}_R.png').astype(int); d=np.abs(a-b).max(2); ys,xs=np.where(d>30)
  print(k,'diff bbox',xs.min()/1696,ys.min()/2528,xs.max()/1696,ys.max()/2528)
