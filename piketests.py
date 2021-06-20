import pikepdf

def loadPdf(fileName):
    currentPdf = pikepdf.open(fileName)
    