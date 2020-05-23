
import cv2
import random
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


'''opencv+PIL 改变图像通道数'''

def change_channels(img):

    # 分离原来图像的通道
    # 使用PIL进行通道分离和合并，先将openCV格式转换为PIL.Image
    pil_image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 分离rgb通道
    r, g, b = pil_image.split()
    channel_list = [r, g, b]
    # 随机打乱顺序后
    random.shuffle(channel_list)
    # 进行通道合并
    new_pil_image = Image.merge('RGB', tuple(channel_list))
    # PIL.Image 格式转换为openCV格式
    new_image = cv2.cvtColor(np.asarray(new_pil_image), cv2.COLOR_RGB2BGR)

    return new_image

if __name__ == '__main__':

    image = cv2.imread('../myimages/7.jpg')

    # 调用改变通道函数
    new_image = change_channels(image)
    # 将新的图片写在本地
    cv2.imwrite('new_image7.jpg', new_image)

    # 也可以在窗口查看效果
    plt.subplot(121), plt.imshow(image), plt.title('Input')
    plt.subplot(122), plt.imshow(new_image), plt.title('Output')
    plt.show()

