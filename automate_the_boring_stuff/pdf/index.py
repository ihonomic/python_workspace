import PyPDF2
#           READ
pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

totalPages = pdfReader.numPages  # attribute to get Total pages

pageObj = pdfReader.getPage(5)  # method to get the needed page
content = pageObj.extractText()  # method to read text

# pdfReader.isEncrypted  # attribute to know if it is encrypted
# pdfReader.decrypt('password')  # method to decrypt


#           WRITE

pdf1Reader = PyPDF2.PdfFileReader(open('meetingminutes.pdf', 'rb'))
pdf2Reader = PyPDF2.PdfFileReader(open('gssi.pdf', 'rb'))

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('combinedPdf.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
