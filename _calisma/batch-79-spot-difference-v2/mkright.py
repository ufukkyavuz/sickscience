import cv2, numpy as np, sys
def load(p): return cv2.imread(p)
S = 1696/600
def box(x0,y0,x1,y1): return [int(v*S) for v in (x0,y0,x1,y1)]
# DropOff: remove cellulite squiggles on thigh
im = load('DO_L.png'); x0,y0,x1,y1 = box(300,525,415,610)
roi = im[y0:y1,x0:x1].astype(int)
lum = roi.mean(2)
outline = (lum<120).astype(np.uint8)
outline = cv2.dilate(outline, np.ones((15,15),np.uint8))
skin = np.median(roi[(lum>200)].reshape(-1,3),0)
diff = np.abs(roi-skin).sum(2)
m = ((diff>45)&(outline==0)&(lum>=120)).astype(np.uint8)*255
m = cv2.dilate(m, np.ones((7,7),np.uint8))
full = np.zeros(im.shape[:2],np.uint8); full[y0:y1,x0:x1]=m
out = cv2.inpaint(im, full, 9, cv2.INPAINT_TELEA)
cv2.imwrite('DO_R.png', out); print('DO mask px', (full>0).sum())
# PowerCycle: fill visible scalp in the parting with hair colour
im = load('PC_L.png'); x0,y0,x1,y1 = box(270,95,345,151)
roi = im[y0:y1,x0:x1].astype(int); lum = roi.mean(2)
hair = np.median(im[box(240,100,260,140)[1]:box(240,100,260,140)[3], box(240,100,260,140)[0]:box(240,100,260,140)[2]].reshape(-1,3),0)
m = ((lum>200)&((roi[:,:,2]-roi[:,:,0])>12)).astype(np.uint8)*255
m = cv2.dilate(m, np.ones((5,5),np.uint8))
out = im.copy(); sub = out[y0:y1,x0:x1]; sub[m>0] = hair.astype(np.uint8)
cv2.imwrite('PC_R.png', out); print('PC hair', hair, (m>0).sum())
