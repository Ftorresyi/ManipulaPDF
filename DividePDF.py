import os
from pikepdf import Pdf

# the target PDF document to split
filename = "bca_do_dia.pdf"
# load the PDF file
arqpdf = Pdf.open(filename)

'''#Next, we make the resulting PDF files (3 in this case) as a list:
# a dictionary mapping PDF file to original PDF's page range
file2pages = {
    0: [0, 9], # 1st splitted PDF file will contain the pages from 0 to 9 (9 is not included)
    1: [9, 11], # 2nd splitted PDF file will contain the pages from 9 (9 is included) to 11
    2: [11, 100], # 3rd splitted PDF file will contain the pages from 11 until the end or until the 100th page (if exists)
}'''

#FUNCIONANDO TOTAL 3
pginit = 10000
file2pages = {}

for i in range(1,5):
    while pginit != 0:
        pginit = int(input('Digite a página inicial da divisão. Tecle Zero par a sair '))
        pgfim = int(input('Digite a página final da divisão. Tecle Zero par a sair '))
        file2pages[i] = [pginit, pgfim]
        i=i+1
        print(file2pages, type(file2pages))
    else: break
print (file2pages, " é um dicionario")

'''In the above setting, we're going to split our PDF file into 3 new PDF documents, the first contains the first 9 pages,
from 0 to 9 (while 9 is not included). The second file will contain the pages from 9 (included) to 11, and the last file
will contain the page range from 11 until the end or until reaching page 100 if it exists.

This way, we assure maximum flexibility as each one of you has its own use case. If you want to split each page into
a new PDF document, you can simply replace [0, 9] to [0], so it'll be a list of one element and that is the first page, and so on.

This is the file we're going to split (you can get it here if you want to follow along):'''

# make the new splitted PDF files
new_pdf_files = [ Pdf.new() for i in file2pages ]
# the current pdf file index
new_pdf_index = 0


'''To make a new PDF file, you simply call the Pdf.new() method. The new_pdf_index variable is the index of the file,
it will only be incremented when we're done with making the previous file. Diving into the main loop:'''

# iterate over all PDF pages
for n, page in enumerate(arqpdf.pages):
    if n in list(range(*file2pages[new_pdf_index])):
        # add the `n` page to the `new_pdf_index` file
        new_pdf_files[new_pdf_index].pages.append(page)
        print(f"[*] Assigning Page {n} to the file {new_pdf_index}")
    else:
        # make a unique filename based on original file name plus the index
        name, ext = os.path.splitext(filename)
        output_filename = f"{name}-{new_pdf_index}.pdf"
        # save the PDF file
        new_pdf_files[new_pdf_index].save(output_filename)
        print(f"[+] File: {output_filename} saved.")
        # go to the next file
        new_pdf_index += 1
        # add the `n` page to the `new_pdf_index` file
        new_pdf_files[new_pdf_index].pages.append(page)
        print(f"[*] Assigning Page {n} to the file {new_pdf_index}")

# save the last PDF file
name, ext = os.path.splitext(filename)
output_filename = f"{name}-{new_pdf_index}.pdf"
new_pdf_files[new_pdf_index].save(output_filename)
print(f"[+] File: {output_filename} saved.")

'''First, we iterate over all the PDF files using the pdf.pages attribute. If the page index is in the file 
page range in the file2pages dictionary, then we simply add the page into our new file. Otherwise, then we 
know we're done with the previous file, and it is time to save it to the disk using save() method, and we 
continue the loop until all pages are assigned to their files. And then finally, we save the last file outside the loop.

Here's the output when I run the code:

[*] Assigning Page 0 to the file 0
[*] Assigning Page 1 to the file 0
[*] Assigning Page 2 to the file 0
[*] Assigning Page 3 to the file 0
[*] Assigning Page 4 to the file 0
[*] Assigning Page 5 to the file 0
[*] Assigning Page 6 to the file 0
[*] Assigning Page 7 to the file 0
[*] Assigning Page 8 to the file 0
[+] File: bert-paper-0.pdf saved.
[*] Assigning Page 9 to the file 1 
[*] Assigning Page 10 to the file 1
[+] File: bert-paper-1.pdf saved.
[*] Assigning Page 11 to the file 2
[*] Assigning Page 12 to the file 2
[*] Assigning Page 13 to the file 2
[*] Assigning Page 14 to the file 2
[*] Assigning Page 15 to the file 2
[+] File: bert-paper-2.pdf saved.'''
