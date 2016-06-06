import os
import re
import sys
import tempfile
import commands
from PyPDF2 import PdfFileWriter, PdfFileReader


num_regex = re.compile('^\d*$', re.UNICODE)
in_fn = sys.argv[-1]
out_fn = tempfile.mktemp(suffix='.txt')
cmd = 'mutool draw -o "{out_fn}" -F text "{in_fn}"'.format(out_fn=out_fn, in_fn=in_fn)
print cmd
status = os.system(cmd)
print status

text = None
page_no = None


result = list()
for line in open(out_fn, 'rb'):
    line = line.strip()
    if not line:
        continue

    if line.startswith('template'):
        text = line.replace(' ', '')

    if num_regex.match(line):
        page_no = line
        if text:
            result.append(dict(page_no=page_no, text=text))
        text = None

print result
    
