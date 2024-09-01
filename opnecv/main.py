import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取彩色图像
image = cv2.imread('tomato1.jpg')
img2 = np.array(image, dtype='int')
b1, g1, r1 = cv2.split(img2)
Toma = r1-g1 
[m, n] = Toma.shape
for i in range(m):
    for j in range(n):
        if Toma[i, j] < 0:
            Toma[i, j] = 0
        elif Toma[i, j] > 255:
            Toma[i, j] = 255
gray = np.array(Toma, dtype='uint8')

median = cv2.medianBlur(gray, 3)#中值滤波
ret1, th1 = cv2.threshold(median, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
hole = th1.copy()
# Find the hole and fill it
cv2.floodFill(hole, None, (0, 0), 255)
hole = cv2.bitwise_not(hole)
filledEdgesOut = cv2.bitwise_or(th1, hole)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#image of corrosion
eroded = cv2.erode(filledEdgesOut,kernel)
def baweraopen(image,size):
    output=image.copy()
    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(image)
    for i in range(1,nlabels-1):
        regions_size=stats[i,4]
        if regions_size<size:
            x0=stats[i,0]
            y0=stats[i,1]
            x1=stats[i,0]+stats[i,2]
            y1=stats[i,1]+stats[i,3]
            for row in range(y0,y1):
                for col in range(x0,x1):
                    if labels[row,col]==i:
                        output[row,col]=0
    return output
region=baweraopen(eroded,200)#
# 使用Canny算子进行边缘检测
edges = cv2.Canny(region, 50, 150, apertureSize=3)


# 霍夫圆检测
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 118, param1=50, param2=32, minRadius=0, maxRadius=0)

# 在原图上绘制检测到的圆
if circles is not None:
    circles = np.round(circles[0, :]).astype('int')
    for x, y, r in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 2)
        cv2.circle(image, (x, y), 2, (0, 0, 255), 3)

    # 显示结果图像
plt.figure(figsize=(100, 50), dpi=80)
plt.subplot(131), plt.imshow(cv2.cvtColor(region, cv2.COLOR_BGR2RGB)), \
plt.title('region',fontsize=100), plt.axis('off')
plt.subplot(132), plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB)), \
plt.title('canny',fontsize=100), plt.axis('off')
plt.subplot(133), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), \
plt.title('Detected Circles',fontsize=100), plt.axis('off')
plt.show()