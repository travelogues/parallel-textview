# Reads the contents of the /data folder and generates an HTML table of contents
from os import listdir
from os.path import isfile, join, exists
import warnings

files = [ f for f in listdir('../data/') if isfile(join('../data/', f)) ]

# TODO verify that text files are available for each barcode

def to_LI(filename):
  barcodes = filename[:-5].split('_')

  if not exists(f'../texts/{barcodes[0]}.txt'):
    warnings.warn(f'File {barcodes[0]} does not exist!')

  if not exists(f'../texts/{barcodes[1]}.txt'):
    warnings.warn(f'File {barcodes[1]} does not exist!')

  return f'<li><a href="index.html#{barcodes[0]},{barcodes[1]}">{barcodes[0]} - {barcodes[1]}</a></li>'

html_list = [ to_LI(f) for f in files ]

with open('../toc.html', 'w') as outfile:
  outfile.write(f"""<html>
    <head>
      <title>Table of Contents</title>
    </head>
    <body>
      <ul>
        {''.join(html_list)}
      </ul>
    </body>
  </html>""")