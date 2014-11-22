# -*- coding: utf-8 -*-
#
#把所有jpg、png、gif文件修改为指定的宽度，高度保持原比例
#图片的高度会忽略小数
#默认处理Windows系统桌面的图片文件
#
#python3.4 Pillow2.6.1
#Pillow is the "friendly" PIL fork, http://python-pillow.github.io/, 在PyPI下载.

from PIL import Image
import os,glob,winreg,sys

tarWidth_str = sys.argv[1]
tarWidth_int = int(tarWidth_str)

def getDesktopPath():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,\
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',)
    return winreg.QueryValueEx(key, "Desktop")[0]

def chImgSize(imgName):
    img = Image.open(imgName)
    (x,y) = img.size
    
    print(imgName.count('.jpg'))
    if x == tarWidth_int:#如果已经是目标尺寸则什么都不做
        if imgName.count('.jpg')>0:#非jpg图片要转换
            return
    if imgName.count('.png'):
        imgName += '.jpg'#直接追加jpg扩展名，简单粗暴
    elif imgName.count('.gif'):
        imgName += '.jpg'
        img = img.convert('RGB')#gif 2 jpg 预处理
    #img.resize((宽, 高-同比例), 算法).save(保存地址-扩展名有变则自动转换, 图片质量)
    print (y*tarWidth_int/x)
    img.resize((tarWidth_int, int(y*tarWidth_int/x)), Image.ANTIALIAS).save(tarWidth_str+"px-"+imgName, quality=90)

if __name__ == '__main__':
    print ("请稍等...事后自动关闭o(^▽^)o")
    #if unicode(os.getcwd(),'GB2312') in getDesktopPath():#Not in 即是桌面的子目录，则处理子目录
    if os.getcwd() in getDesktopPath():
        os.chdir(getDesktopPath())
    imgNames = glob.glob('*.jpg') + glob.glob('*.png') + glob.glob('*.gif')
    for imgName in imgNames:
        chImgSize(imgName)
    #raw_input()
