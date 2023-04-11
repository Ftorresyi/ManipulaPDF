from tabula import convert_into #pip install tabula-py
import tabula
import pdftables_api

#df = tabula.read_pdf("Extrato-Efetivo.pdf", pages='all')
#print(df[1]) # imprime a primeira tabela encontrada na página 6 do PDF.

table_file = r"Extrato-Efetivo.pdf"
output_csv = r"dados.csv"

#df = convert_into(table_file, output_csv, output_format='csv', lattice=True, stream=False, pages="1")

c = pdftables_api.Client('seu API key')
c.csv('input.pdf', 'output.csv')