import unicodedata
import cv2
import pytesseract
from fpdf import FPDF
import io

text_to_pdf = FPDF()#take str to pd


text_to_pdf.add_page() #add page


#select font style and size
text_to_pdf.set_font("Arial",size = 14)

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('img/2022-02-23_001.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


str_of_img = pytesseract.image_to_string(img)

print(str_of_img)


def strip_accents(str_of_img):
    return ''.join(char for char in
                   unicodedata.normalize('NFKD', str_of_img)
                   if unicodedata.category(char) != 'Mn')

with io.open('output_txt.txt',"w" ,encoding="utf-8") as i:
    i.write(str_of_img)


f = open("output_txt.txt",'r',encoding="utf8")

#setup page sell
for i in f:
    text_to_pdf.cell(200, 10, txt = i, ln = 1, align = 'C')


text_to_pdf.output("img.pdf")
cv2.imshow('Img2Str',img)
cv2.waitKey(0)




