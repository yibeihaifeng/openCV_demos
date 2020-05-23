


import numpy as np
import cv2
import matplotlib.pyplot  as plt

'''改变对比度和亮度'''

def change_contrast(Image):

    blank = np.zeros(Image.shape, Image.dtype)
    # dst = alpha * img + beta * blank
    # 假设对比度为1.2，亮度为10
    dst = cv2.addWeighted(Image, 1.5, blank, 1 - 1.5, 10)

    return dst



if __name__ == '__main__':
    image = cv2.imread('../myimages/3.jpg')
    # 图片原来的固有字段的坐标及值
    points_list = []
    with open('../myimages/gt_3.txt','r',encoding='utf-8') as f:
        for line in f.readlines():
            # 获取前8个元素，也就是四点坐标，后面的是文本内容，可以不用变
            data_line = line.split(',')
            # 将列表中坐标元素变成int
            data =  [ int(i) if data_line.index(i)<=7  else i for i in data_line]
            points_list.append(data)
    print(points_list)
    # 开始调节
    new_image = change_contrast(image)
    # 将新的图片写在本地
    cv2.imwrite('new_image3.jpg',new_image)

    # 也可以在窗口查看效果
    plt.subplot(121), plt.imshow(image), plt.title('Input')
    plt.subplot(122), plt.imshow(new_image), plt.title('Output')
    plt.show()
