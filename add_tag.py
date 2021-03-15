import nbformat as nbf
from glob import glob
import sys

TAG = sys.argv[-1]

assert len(sys.argv) == 2

notebooks = glob("./content/**/*.ipynb", recursive=True)

# Search through each notebook and look for th text, add a tag if necessary
for ipath in notebooks:
    ntbk = nbf.read(ipath, nbf.NO_CONVERT)

    for cell in ntbk.cells:
        if cell['cell_type'] == 'code':
            cell_tags = cell['metadata'].get('tags', [])
            if not TAG in cell_tags:
                cell_tags.append(TAG)
            cell['metadata']['tags'] = cell_tags

    with open(ipath, 'w', encoding='utf-8') as f:
        nbf.write(ntbk, f)
