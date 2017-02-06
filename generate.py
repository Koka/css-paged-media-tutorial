

import os
import zipfile
import glob
import shutil
import subprocess
import tempfile


MASTER = os.path.abspath(os.getcwd())
TARGET = os.path.join(tempfile.gettempdir(), 'generated')

if os.path.exists(TARGET):
    shutil.rmtree(TARGET)

shutil.copytree('styles', os.path.join(TARGET, 'styles'))
shutil.copy('Makefile', TARGET)

for i, name in enumerate(glob.glob('lesson-*')):
    print(name)

    source_dir = os.path.join(MASTER, name)
    workdir = os.path.join(TARGET, name)
    print(workdir)
    shutil.copytree(source_dir, workdir)
    p = subprocess.Popen('make', cwd=workdir)
    print(p.wait())



zip_fn = os.path.join(MASTER, 'generated.zip')
ZF = zipfile.ZipFile(zip_fn, 'w')

for dirname, dirnames, filenames in os.walk(TARGET):
    for name in filenames:
        fullname = os.path.join(dirname, name)
        zip_name = fullname.replace(TARGET + '/', '')
        with open(fullname, 'rb') as fp:
            ZF.writestr(zip_name, fp.read())


ZF.close()
    
cmd = 'git add {}'.format(zip_fn)
print(cmd)
print(os.system(cmd))

cmd = 'git commit -m updated {}'.format(zip_fn)
print(cmd)
print(os.system(cmd))
