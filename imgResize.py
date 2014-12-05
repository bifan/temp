# -*- coding: utf-8 -*-
#
#把所有jpg、png、gif文件修改为指定的宽度, 高度保持原比例, 高度会忽略小数
#处理当前目录的图片, 处理后的图片重命名并保存在当前目录(重命名格式: width-oldFileName.jpg)
#如果用Win+R执行会处理Windows系统桌面的图片文件
#
#python3.4 Pillow2.6.1
#Pillow is the "friendly" PIL fork, http://python-pillow.github.io/, 在PyPI下载.

from PIL import Image
import os,glob,winreg,sys

tarWidth_str = sys.argv[1]#sys.argv[0]是当前文件的路径
tarWidth_int = int(tarWidth_str)

PROCESS_MSG = ""

def getDesktopPath():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,\
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',)
    return winreg.QueryValueEx(key, "Desktop")[0]

def imgOk(x, imgName):
    return x == tarWidth_int and imgName.endswith(".jpg")

def toJpg(imgName, img):
    global PROCESS_MSG
    if imgName.endswith('.png'):
        imgName += '.jpg'#直接追加jpg扩展名，简单粗暴
        PROCESS_MSG += ".png2jpg"
    elif imgName.endswith('.gif'):
        imgName += '.jpg'
        img = img.convert('RGB')#gif 2 jpg 预处理
        PROCESS_MSG += ".gif2jpg"
    return (imgName,img)
    
def chImgSize(imgName):
    global PROCESS_MSG
    PROCESS_MSG = ""
    
    img = Image.open(imgName)
    (x,y) = img.size
    
    if imgOk(x, imgName):
        PROCESS_MSG += ".doNothing"
        return PROCESS_MSG
    else:
        img = img.resize((tarWidth_int, int(y*tarWidth_int/x)), Image.ANTIALIAS)#resize((宽, 高), 算法)
        PROCESS_MSG += ".resize"
    (imgName,img) = toJpg(imgName, img)
    
    if(img.mode == "CMYK"):#如果是CMYK则转成RGB
        img = img.convert("RGB")
    
    img.save(tarWidth_str+"-"+imgName, quality=90)#save(保存路径, 图片质量)
    return PROCESS_MSG

#为了美化输出结果
def niceTip(tip):
    for index in range(22-len(tip)):
        tip += "-"
    return tip

if __name__ == '__main__':
    desktopPath = getDesktopPath()
    #如果用Win+R执行, 当前路径为windows桌面的父目录, 需要把路径指向桌面
    if os.getcwd() in desktopPath:
        os.chdir(desktopPath)
    imgNames = glob.glob('*.jpg') + glob.glob('*.png') + glob.glob('*.gif')#得到图片文件名数组
    
    print ("")
    for index,imgName in enumerate(imgNames):
        processMsg = chImgSize(imgName)
        tip = "img"+str(index)+processMsg
        tip = niceTip(tip)+"("+imgName+")"
        print (tip)
    print ("")
