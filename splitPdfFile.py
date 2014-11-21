# -*- coding: utf-8 -*-
#需要模块：http://pybrary.net/pyPdf/
#
from pyPdf import PdfFileWriter, PdfFileReader

filePath = "" #"fileName.pdf"
splitPages = 200 #默认每200页进行一次分割

inputpdf = PdfFileReader(open(filePath, "rb"))
output = PdfFileWriter()

for i in xrange(inputpdf.numPages):
    
    if(i==0):#0可以整除splitPages，会产生一张只有一页的PDF文件
        continue
    
    output.addPage(inputpdf.getPage(i))
    
    #能够整除splitPages时，输出这部分PDF
    if((i)%splitPages==0):
        outputStream = file(str(i)+".pdf", "wb")
        output.write(outputStream)
        outputStream.close()
        output = PdfFileWriter()#输出后开始一个新的，不然会保留已输出的页
        print str(i)+" split PDF"

    #最后一部分pdf文件，在最后一次for循环时输出。
    if(inputpdf.numPages == i+1):
        outputStream = file(str(i)+".pdf", "wb")
        output.write(outputStream)
        outputStream.close()
        print str(i)+" last PDF"
        

