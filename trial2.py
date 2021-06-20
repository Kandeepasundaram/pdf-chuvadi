import pikepdf
# my_pdf = 
# for page in my_pdf.pages:
#    page.Rotate = 180
# my_pdf.save('test-rotated.pdf')

def decodeACopy(filename):
    print (filename)
    pdf = pikepdf.Pdf.open(filename)
    newFilename = filename + '_decoded.pdf';
    pdf.save(newFilename)
    return newFilename


    
    