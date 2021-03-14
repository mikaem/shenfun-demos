from glob import glob
import re
htmls = glob("./_build/html/**/*.html", recursive=True)
for html in htmls:
    try:
        b = open(html)
        bs = b.read()
        b.close()
        bs = re.sub('thebelab@latest', 'thebe-mikaem', bs)
        b = open(html, 'w')
        b.write(bs)
        b.close()
    except:
        pass