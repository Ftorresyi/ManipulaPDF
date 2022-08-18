#from PyPDF3 import PdfFileWriter, PdfFileReader
import fitz

arquivo_pdf = input("Digite o nome do arquivo PDF: " )
inputpdf = fitz.open(arquivo_pdf)

pag_inicial = input("Digite a página inicial para dividir: ")

pag_final = input("Digite a página final para dividir: ")

inputpdf.insertPDF()