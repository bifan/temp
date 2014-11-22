**simulateEclipsePlugin.vim**
>vim插件 (Windows)
>模仿eclipse的一些快捷键

==================================
**splitPdfFile.py**
>Python代码 (Windows)

>分割PDF文件

==================================
**imgResize.py**
>Python代码 (Windows)

>根据指定宽度批量修改图片文件(jpg\gif\png)的尺寸, 保持比例, 统一另存为jpg文件

>使用\*.bat文件调用, 把\*.bat和imgResize.py放在同一文件夹并加入环境变量

>需求宽度是固定的几个, 所以用批处理调用可以省去 参数、扩展名

>批处理例子: *to700.bat*
```
@echo off
imgResize.py 700
pause
exit
```
>快捷键*Winr+R*打开运行窗口输入*to700*, 执行后会有类似提示:
```
img0.doNothing--------(700width.jpg)
img1.resize.gif2jpg---(1200width.gif)
请按任意键继续. . .
```
