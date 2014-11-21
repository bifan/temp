#需要模块：http://pybrary.net/pyPdf/
#Demo：一个约1000页的pdf code.pdf
#      以500页为界分割为两个pdf
from pyPdf import PdfFileWriter, PdfFileReader

filePath = ""
maxPages = 0


inputpdf = PdfFileReader(open("code.pdf", "rb"))
output1 = PdfFileWriter()
output2 = PdfFileWriter()
for i in xrange(inputpdf.numPages):
    if(i<500):
        output1.addPage(inputpdf.getPage(i))
    if(i>500):
        output2.addPage(inputpdf.getPage(i))
outputStream1 = file("code1.pdf", "wb")
outputStream2 = file("code2.pdf", "wb")
output1.write(outputStream1)
output2.write(outputStream2)
outputStream1.close()
outputStream2.close()
