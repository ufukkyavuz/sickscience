import cv2, numpy as np
S=1696/600; im=cv2.imread('NW_L.png'); ox,oy=int(160*S),int(230*S)
c=im[oy:oy+537, ox:ox+678].copy(); ci=c.astype(int)
skin=ci[110:130,320:340].reshape(-1,3).mean(0)
d=np.abs(ci-skin).sum(2)
m=np.zeros(d.shape,np.uint8)
for (x0,y0,x1,y1) in [(68,182,212,356),(372,182,600,345)]:
    m[y0:y1,x0:x1]=(d[y0:y1,x0:x1]>28).astype(np.uint8)*255
m[150:310,225:305]=0
m=cv2.dilate(m,np.ones((7,7),np.uint8))
c=cv2.inpaint(c,m,9,cv2.INPAINT_TELEA).astype(float)
# soft glow on the cheekbones
g=np.zeros(d.shape,np.float32)
for (cx,cy) in [(135,215),(505,210)]:
    cv2.ellipse(g,(cx,cy),(62,34),-12 if cx<300 else 12,0,360,1.0,-1)
g=cv2.GaussianBlur(g,(0,0),18)*0.45
c=c*(1-g[...,None])+np.array([235,240,255.0])*g[...,None]
sp=np.zeros(d.shape,np.float32)
for (cx,cy) in [(120,200),(490,195)]:
    cv2.ellipse(sp,(cx,cy),(16,7),-20 if cx<300 else 20,0,360,1.0,-1)
sp=cv2.GaussianBlur(sp,(0,0),2.5)*0.85
c=c*(1-sp[...,None])+255*sp[...,None]
out=im.copy(); out[oy:oy+537, ox:ox+678]=c.astype(np.uint8); cv2.imwrite('NW_R.png',out)
cv2.imwrite('/tmp/claude-501/nw_face_r.png', out[oy:oy+537, ox:ox+678])
a=im.astype(int); b=out.astype(int); dd=np.abs(a-b).max(2); ys,xs=np.where(dd>20); print('NW diff bbox',xs.min()/1696,ys.min()/2528,xs.max()/1696,ys.max()/2528)
