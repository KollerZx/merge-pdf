import PyPDF2
import os

# TODO: Implementar uma forma de definir a ordem em que os pdf's serão mesclados

files_list = os.listdir('src/uploads')
merger = PyPDF2.PdfFileMerger()

for file in files_list:
  if ".pdf" in file:
    merger.append(f'src/uploads/{file}')

merger.write('src/merged.pdf')