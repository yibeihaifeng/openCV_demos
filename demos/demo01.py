import cv2
import math
import random
import numpy as np
import matplotlib.pyplot  as plt


'''图片倾斜，缩放'''

def rotate_bound(Image,total_points_list):

    angle = random.choice([random.randint(0,45),90,180,270])  # 获取随机旋转角度
    # 随机缩放
    scale = 1
    if random.randint(0,1)==0: # 不进行缩放
        pass
    else:
        scale=round(random.uniform(0.5,1.5),1) # 缩放因子

    w = Image.shape[1]
    h = Image.shape[0]
    rangle = np.deg2rad(angle)
    nw = (abs(np.sin(rangle) * h) + abs(np.cos(rangle) * w)) * scale
    nh = (abs(np.cos(rangle) * h) + abs(np.sin(rangle) * w)) * scale
    M = cv2.getRotationMatrix2D((w * 0.5, h * 0.5), angle, scale)
    nw = max(w, nw)
    nh = max(h, nh)
    M[0, 2] += (nw - w) / 2
    M[1, 2] += (nh - h) / 2
    new_image = cv2.warpAffine(Image, M, (int(math.ceil(nw)), int(math.ceil(nh))))
    if angle<=45:
        # 获取变换后的坐标
        total_points_list =get_points(total_points_list,M)


    elif angle==90:
        total_points_list = get_points(total_points_list, M)
        for i in total_points_list:
            i[0], i[1],i[2], i[3],i[4], i[5],i[6], i[7] =i[2], i[3],i[4], i[5],i[6], i[7], i[0], i[1]



    elif angle==180:
        total_points_list = get_points(total_points_list, M)
        for i in total_points_list:
            i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7] = i[4], i[5],i[6], i[7],i[0], i[1],i[2], i[3]


    elif angle==270:
        total_points_list = get_points(total_points_list, M)
        for i in total_points_list:
            i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]= i[6], i[7],i[0], i[1],i[2], i[3],i[4], i[5]


    return new_image,total_points_list


def get_points(points_list, M):
    '''坐标转换'''
    for i in points_list:
        i[0], i[1] = [int(i) for i in list(np.dot(M, np.array([i[0], i[1], 1])))]
        i[2], i[3] = [int(i) for i in list(np.dot(M, np.array([i[2], i[3], 1])))]
        i[4], i[5] = [int(i) for i in list(np.dot(M, np.array([i[4], i[5], 1])))]
        i[6], i[7] = [int(i) for i in list(np.dot(M, np.array([i[6], i[7], 1])))]

    return points_list

if __name__ == '__main__':
    image = cv2.imread('../myimages/1.jpg')
    # 图片原来的固有字段的坐标及值
    points_list = []
    # 这里txt文本的每行格式为      x1,y2,x2,y2,x3,y3,x4,y4,0,'文本内容'       其中前面8个点为该文本内容的顺时针四个点的坐标，第一个为左上角
    with open('../myimages/gt_1.txt','r',encoding='utf-8') as f:
        for line in f.readlines():
            # 获取前8个元素，也就是四点坐标，后面的是文本内容，可以不用变
            data_line = line.split(',')
            # 将列表中坐标元素变成int
            data =  [ int(i) if data_line.index(i)<=7  else i for i in data_line]
            points_list.append(data)

    # 开始旋转
    new_image,points_list = rotate_bound(image,points_list)
    # 将新的图片写在本地
    cv2.imwrite('new_image.jpg',new_image)
    # 将新的坐标也写在本地
    f = open('new_image.txt', 'w', encoding='utf-8')

    for lab in points_list:
        line = ",".join(str(i) for i in lab)
        f.write(line)
        f.write('\n')
    f.close()

    # 也可以在窗口查看效果
    plt.subplot(121), plt.imshow(image), plt.title('Input')
    plt.subplot(122), plt.imshow(new_image), plt.title('Output')
    plt.show()


