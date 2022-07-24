from asyncio.format_helpers import extract_stack
import PyPDF2
import os
import re


def askUser():

    print("\nEntrer le nom du pdf que vous voulez examiner : ", end = "") #testpdf
    nomPdf=input()
    if len(nomPdf) == 0: 
        raise Exception("Nom de pdf invalide")

    print("\nEntrer le numéro de la pompe : ", end = "") #Ligne4
    numPompe = input()
    if len(numPompe) == 0:
        raise Exception("Aucun mot fourni, veuillez rééssayer ! ")

    return nomPdf, numPompe

def findFile(serialNumber):
    dossier = os.getcwd()
    pdfRepo="%s/ressources/%s.pdf" % (dossier, serialNumber)
    return pdfRepo

def extractTemplate(stripped):
    data=stripped[0:8]
    matricola=stripped[26:40]
    Qlpm=stripped[70:74]
    return data,matricola,Qlpm

def _extractText(pdf):

    pdfFileObj = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfText = ""

    for page in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(page)
        pdfText += pageObj.extract_text()
    textSplit=list(pdfText.split('\n'))
    # rangement du texte dans une liste 2 dimensions (lignes et mots)
#    print("Text split : ",textSplit)
#    textOrdered = [[]]
    textOrdered = []

    for word in textSplit:
        stripped = word.strip()
        if re.search(r"\d+/\d+/\d*",stripped) :
            data,matricola,Qlpm=extractTemplate(stripped)
            res = "La pompe %s à été testé le %s et la valeur Q(lpm) est : %s"% (matricola, data, Qlpm)
            textOrdered.append(res)
#    print("text Ordered : ", textOrdered)
    return textOrdered


def extractLigne(pdf, numPompe):
    textSplit = _extractText(pdf)
    return textSplit[int(numPompe)-1]
## Retourner la date du test (data), le matricule de la pompe (matricola) avec le Qlpm (en noir)  