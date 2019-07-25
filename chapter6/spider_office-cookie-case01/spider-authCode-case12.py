'''
识别简单图片验证码
'''
from PIL import Image
import pytesseract

def test01():
    # 图片实例
    image = Image.open(r'f:/4.png')
    # 转换后的结果
    text = pytesseract.image_to_string(image)
    print(text)
if __name__ == '__main__':
    test01()