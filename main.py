from tkinter import Tk, filedialog
from tkinter.ttk import *
from trial2 import *
import PyPDF2

ONE_SHEET = 4

root = Tk()

root.title("SeraCorp PDF Chuvadi");

# frame inside root window
frame = Frame(root)                  
# geometry method
frame.grid()  

label = Label(frame, text="Load PDF")
label.grid()

root.numPages = 0


def loadPdfFile(filename):
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    d = dict(); 
    d['pdfFileObj']   = pdfFileObj
    d['pdfReader'] = pdfReader
    return d

def calculateSignatures():
    sheetsPerSignature = Entry()
    sheetsPerSignatureEntry = sheetsPerSignature.get()
    # estimatedSignaturesLabel = Label(frame, text="Estimated Signatures: " + root.numPages/sheetsPerSignatureEntry)
    # estimatedSignaturesLabel.grid()
    for i in range(6):
        print(f'One Sheet has {ONE_SHEET}')
        print(f'Using {i + 1} sheets in a signature')
        print(f'Total Signatures will be : {root.numPages//((i+1)*ONE_SHEET)}')
        print(f'Orpahned pages count is : {root.numPages%((i+1)*ONE_SHEET)}')
        print('-----------------------------------------------------------------')

def selectFile():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select PDF", filetypes = (("pdf files","*.pdf"),("all files","*.*")))
    print (root.filename)
    loadedDict = loadPdfFile(root.filename)
    root.pdfFileObj, pdfReader = loadedDict['pdfFileObj'], loadedDict['pdfReader']
    if pdfReader.isEncrypted:
        print('Inside Decryption')
        decodedFileName = decodeACopy(root.filename)
        loadedDict = loadPdfFile(decodedFileName)
        root.pdfFileObj, pdfReader = loadedDict['pdfFileObj'], loadedDict['pdfReader']
    root.numPages = pdfReader.numPages
    print(f'Number of Pages in the document is : {root.numPages}')
    print(f'Named Destinations are : {pdfReader.namedDestinations}')
    print(f'Page Layout is : {pdfReader.pageLayout}')    
    # numberOfPagesLabel = Label(frame, text="Total Pages: " + root.numPages)
    

selectPdfBtn = Button(frame, text ='Select PDF', command = selectFile)  
selectPdfBtn.grid()    

calcSignBtn = Button(frame, text ='Calculate Signatures', command = calculateSignatures)  
calcSignBtn.grid()   

exitBtn = Button(frame, text ='Exit', command = root.destroy)  
exitBtn.grid()   
if hasattr(root,'pdfFileObj'):
    root.pdfFileObj.close()


root.mainloop()
    
    