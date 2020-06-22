import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

class Camaras():
    def __init__(self):
        # Camara izquierda
        self.cap1 = cv2.VideoCapture(0)
        self.cap1.set(3, 1280)
        self.cap1.set(4, 960)
        self.cap1.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('M','J','P','G'))

        # Camara derecha
        self.cap2 = cv2.VideoCapture(2)
        self.cap2.set(3, 1280)
        self.cap2.set(4, 960)
        self.cap2.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('M','J','P','G'))
    
    def Fotos(self):
        ret1, frameL = self.cap1.read()
        self.cap1.release()

        ret2, frameR = self.cap2.read()
        frameR = cv2.rotate(frameR, cv2.ROTATE_180)
        self.cap2.release()

        sclp = 0.1
        wth = int(1280* sclp)
        hht = int(960 * sclp)

        framel = cv2.resize(frameL, (wth, hht))
        framer = cv2.resize(frameR, (wth, hht))

        return frameL, frameR, framel, framer

def binFondos(img,b):
    R = len(img)
    C = len(img[0])
    
    out = [[False for c in range(C)] for r in range(R)]
    for r in range(R):
        for c in range(C):
            if 3*img[r][c][0] >= sum(img[r][c]) + 2*b:
                out[r][c] = True
    
    maxim1, maxim2 = 0, 0
    grid1, grid2 = [], []
    for r in range(R):
        for c in range(C):
            if out[r][c]:
                out[r][c] = False
                count = 1 
                queue = [(r,c)]
                island = [(r,c)]
                while queue:
                    follow = []
                    for (i,j) in queue:
                        for (ii,jj) in [(-1,0),(1,0),(0,-1),(0,1)]:
                            m = i + ii
                            n = j + jj
                            if 0 <= m and m < R and 0 <= n and n < C:
                                if out[m][n] == True:
                                    count += 1
                                    out[m][n] = False
                                    follow.append((m,n))
                                    island.append((m,n))
                    queue = follow
                if maxim1 < count:
                    maxim1, maxim2 = count, maxim1
                    grid1, grid2 = island, grid1
                elif maxim2 < count:
                    maxim2 = count
                    grid2 = island

    fx1 = [0 for c in range(C)]
    fy1 = [0 for r in range(R)]
    for (r,c) in grid1:
        fx1[c] += 1
        fy1[r] += 1
    x1 = [(c+1)*fx1[c] for c in range(C)]
    y1 = [(r+1)*fy1[r] for r in range(R)]
    cx1 = int(round(sum(x1)/sum(fx1),0)) # Center X 1st biggest
    cy1 = int(round(sum(y1)/sum(fy1),0)) # Center Y 1st biggest

    fx2 = [0 for c in range(C)]
    fy2 = [0 for r in range(R)]
    for (r,c) in grid2:
        fx2[c] += 1
        fy2[r] += 1
    x2 = [(c+1)*fx2[c] for c in range(C)]
    y2 = [(r+1)*fy2[r] for r in range(R)]
    cx2 = int(round(sum(x2)/sum(fx2),0)) # Center X 2nd biggest
    cy2 = int(round(sum(y2)/sum(fy2),0)) # Center Y 2nd biggest

    if cx1 <= cx2: # Circulo izquierdo - Circulo derecho
        xl,yl,xr,yr = cx1,cy1,cx2,cy2
    else:
        xl,yl,xr,yr = cx2,cy2,cx1,cy1
        
    return xl, yl, xr, yr

def getFondos(img,b,xl,yl,xr,yr):
    R = len(img)
    C = len(img[0])

    fx1 = [0 for c in range(C)]
    fy1 = [0 for r in range(R)]
    for r in range(10*yl-50,10*yl+50):
        for c in range(10*xl-50,10*xl+50):
            if 3*img[r][c][2] >= sum(img[r][c]) + 2*b:
                fx1[c] += 1
                fy1[r] += 1    
    x1 = [(c+1)*fx1[c] for c in range(C)]
    y1 = [(r+1)*fy1[r] for r in range(R)]
    nxl = int(round(sum(x1)/sum(fx1),0)) #Center left X
    nyl = int(round(sum(y1)/sum(fy1),0)) #Center left Y

    fx2 = [0 for c in range(C)]
    fy2 = [0 for r in range(R)]
    for r in range(10*yr-50,10*yr+50):
        for c in range(10*xr-50,10*xr+50):
            if 3*img[r][c][2] >= sum(img[r][c]) + 2*b:
                fx2[c] += 1
                fy2[r] += 1
    x2 = [(c+1)*fx2[c] for c in range(C)]
    y2 = [(r+1)*fy2[r] for r in range(R)]
    nxr = int(round(sum(x2)/sum(fx2),0)) #Center right X
    nyr = int(round(sum(y2)/sum(fy2),0)) #Center right Y

    return nxl, nyl, nxr, nyr

def Coordenadas(lx,ly,rx,ry):
    print('[',lx,ly,'] - [',rx,ry,']')
    #   [x1,y1]   Camaras   [x2,y2]
    #   Izquierda           Derecha
    
    b = 8.04            # Distancia focal
    f = 1455            # [ { 1280/(2 * tan(47.5/2)) } + { 960/(2 * tan(36.5/2)) } ] / 2
    tl = 0.4400105309   # tan(47.5/2)
    th = 0.3297505471   # tan(36.5/2)

    dx = lx - rx
    d = b*f/dx
    print(d)
    er = 1.976-0.11826*d+0.00165*d*d
    zf = d+er

    l = 2*tl*zf
    nx1 = l*(lx-640)/1280
    nx2 = l*(rx-640)/1280
    xf = (nx1+nx2)/2

    h = 2*th*zf
    ny1 = h*(480-ly)/960
    ny2 = h*(480-ry)/960
    yf = (ny1+ny2)/2
    
    return (xf,yf,zf)

def Angulo(xl,yl,zl,xr,yr,zr,theta):
    al = theta + np.arctan(yl/zl)
    ar = theta + np.arctan(yr/zr)
    
    cl = np.cos(al)
    cr = np.cos(ar)
    
    dl = ( (zl*zl + yl*yl)**0.5 ) * cl
    dr = ( (zr*zr + yr*yr)**0.5 ) * cr
    
    print(dl, dr)
    
    delta = np.arctan((dr-dl)/(xr-xl))
    
    return np.rad2deg(delta)

cams = Camaras()
imgL, imgR, imgl, imgr = cams.Fotos()

lxl,lyl,lxr,lyr = binFondos(imgl,70)
rxl,ryl,rxr,ryr = binFondos(imgr,70)
print(lxl,lyl,lxr,lyr)
print(rxl,ryl,rxr,ryr)

nlxl,nlyl,nlxr,nlyr = getFondos(imgL,70,lxl,lyl,lxr,lyr)
nrxl,nryl,nrxr,nryr = getFondos(imgR,70,rxl,ryl,rxr,ryr)
print(nlxl,nlyl,nlxr,nlyr)
print(nrxl,nryl,nrxr,nryr)

(xl,yl,zl) = Coordenadas(nlxl,nlyl,nrxl,nryl) # Circulo izquierdo
(xr,yr,zr) = Coordenadas(nlxr,nlyr,nrxr,nryr) # Circulo derecho
print(xl,yl,zl)
print(xr,yr,zr)

theta = 0
delta = Angulo(xl,yl,zl,xr,yr,zr,theta)
print(delta)

#plt.subplot(121)
#plt.imshow(imgL)
#plt.subplot(122)
#plt.imshow(imgR)
#plt.show()
