import lib
import re 
#########################################
# Le type colonne est le pdf 654321.pdf #
# Le type ligne est le pdf 123456.pdf   #
#########################################
  
if __name__ == '__main__': 

    nomPdf, numPompe = lib.askUser()
    
    pdf = lib.findFile(nomPdf)
    res = lib.extractLigne(pdf, numPompe)

    if res is not None:
        print(res)

