import io 
from py_mining_pdf.pdfinterp import PDFResourceManager, PDFPageInterpreter
from py_mining_pdf.converter import TextConverter
from py_mining_pdf.layout import LAParams
from py_mining_pdf.pdfpage import PDFPage
import os
import sys, getopt

#converts pdf, returns its text content as a string
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf
            text = convert(pdfFilename) #get string of text content of pdf
            textFilename = txtDir + pdf + ".txt"
            textFile = open(textFilename, "w") #make text file
            textFile.write(text) #write text to text file
			#textFile.close

pdfDir = "C:/Users/hp/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.8/pdftotext/pdf"
txtDir = "C:/Users/hp/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.8/pdftotext/text/"
convertMultiple(pdfDir, txtDir)
