from PIL import Image


import numpy as np
import cv2
import random
import matplotlib.pyplot  as plt

'''仿射变换'''

def perspective_transformation(Image,total_points_list):
    '''仿射变换'''
    h, w, ch = Image.shape  # 获取行数（高）和列数（宽）
    # 原图四角坐标
    pts1 = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1]])
    # 像素变化
    px_dif = random.randint(0, 50)
    # 期望得到的图四角坐标
    pts2 = np.float32([[0, 0], [px_dif, h - px_dif], [w - px_dif, h - px_dif]])

    # 获得变换矩阵
    M = cv2.getAffineTransform(pts1, pts2)
    # 应用
    dst = cv2.warpAffine(Image, M, (w, h))

    total_points_list = get_points(total_points_list,M)

    return dst,total_points_list

def get_points(points_list,M):
    '''坐标转换'''
    for i in points_list:
        i[0], i[1] = [int(i) for i in list(np.dot(M, np.array([i[0], i[1], 1])))]
        i[2], i[3] = [int(i) for i in list(np.dot(M, np.array([i[2], i[3], 1])))]
        i[4], i[5] = [int(i) for i in list(np.dot(M, np.array([i[4], i[5], 1])))]
        i[6], i[7] = [int(i) for i in list(np.dot(M, np.array([i[6], i[7], 1])))]

    return points_list



if __name__ == '__main__':
    image = cv2.imread('../myimages/2.jpg')
    # 图片原来的固有字段的坐标及值
    points_list = []
    with open('../myimages/gt_2.txt','r',encoding='utf-8') as f:
        for line in f.readlines():
            # 获取前8个元素，也就是四点坐标，后面的是文本内容，可以不用变
            data_line = line.split(',')
            # 将列表中坐标元素变成int
            data =  [ int(i) if data_line.index(i)<=7  else i for i in data_line]
            points_list.append(data)
    print(points_list)
    # 开始进行仿射变换
    new_image,points_list = perspective_transformation(image,points_list)
    # 将新的图片写在本地
    cv2.imwrite('new_image2.jpg',new_image)
    # 将新的坐标也写在本地
    f = open('new_image2.txt', 'w', encoding='utf-8')

    for lab in points_list:
        line = ",".join(str(i) for i in lab)
        f.write(line)
        f.write('\n')
    f.close()

    # 也可以在窗口查看效果
    plt.subplot(121), plt.imshow(image), plt.title('Input')
    plt.subplot(122), plt.imshow(new_image), plt.title('Output')
    plt.show()