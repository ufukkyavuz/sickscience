import cv2, numpy as np
S=1696/600
im=cv2.imread('NW_L.png'); ox,oy=int(80*S),int(280*S)
c=im[oy:oy+622, ox:ox+339].copy(); lum=c.astype(int).mean(2)
m=np.zeros(lum.shape,np.uint8); r=(slice(325,380),slice(130,235))
m[r]=(lum[r]<60).astype(np.uint8)*255
m=cv2.dilate(m,np.ones((5,5),np.uint8))
c=cv2.inpaint(c,m,5,cv2.INPAINT_TELEA)
im[oy:oy+622, ox:ox+339]=c; cv2.imwrite('NW_L.png',im); cv2.imwrite('/tmp/claude-501/nw_bot2.png',c); print((m>0).sum())
