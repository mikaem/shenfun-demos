import nbformat as nbf
from glob import glob

notebooks = glob("./content/**/*.ipynb", recursive=True)

for ipath in notebooks:
    ntbk = nbf.read(ipath, nbf.NO_CONVERT)
    ntbk['metadata']['kernelspec'] = {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    }
    ntbk['metadata']["language_info"] = {
        "file_extension": ".py",
        "mimetype": "text/x-python",
        "name": "python",
        "nbconvert_exporter": "python",
        "pygments_lexer": "ipython3",
        "version": "3.8.5"
    }
    with open(ipath, 'w', encoding='utf-8') as f:
        nbf.write(ntbk, f)
