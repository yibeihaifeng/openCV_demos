
import random
import matplotlib.pyplot as plt
from PIL import Image


'''使用PIL 进行图像通道变换'''
def change_channels(img):
    '''改变图像通道数'''
    # 读取原来图像的通道
    r,g,b = img.split()
    channel_list = [r,g,b]
    # 随机打乱顺序后
    random.shuffle(channel_list)
    # 进行通道合并
    new_image = Image.merge('RGB',tuple(channel_list))
    return new_image




if __name__ == '__main__':
    image = Image.open('../myimages/4.jpg')
    new_image = change_channels(image)
    new_image.save('new4.jpg')


    # 也可以在窗口查看效果
    plt.subplot(121), plt.imshow(image), plt.title('Input')
    plt.subplot(122), plt.imshow(new_image), plt.title('Output')
    plt.show()


    '''
      使用PIL进行通道分离和合并
      # openCV格式转换为PIL.Image
      pil_image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
      r,g,b = pil_image.split()
      channel_list = [r,g,b]
      # 随机打乱顺序后
      random.shuffle(channel_list)
      # 进行通道合并
      new_pil_image = Image.merge('RGB',tuple(channel_list))
      new_image = cv2.cvtColor(np.asarray(new_pil_image), cv2.COLOR_RGB2BGR)
      # PIL.Image 格式转换为openCV
      '''