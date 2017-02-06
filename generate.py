

import os
import glob
import shutil
import subprocess


MASTER = os.path.abspath(os.getcwd())
TARGET = os.path.join(os.getcwd(), 'generated')

if os.path.exists(TARGET):
    shutil.rmtree(TARGET)

shutil.copytree('styles', os.path.join(TARGET, 'styles'))
shutil.copy('Makefile', TARGET)

for name in glob.glob('lesson-*'):
    print name

    source_dir = os.path.join(MASTER, name)
    workdir = os.path.join(TARGET, name)
    print workdir
    shutil.copytree(source_dir, workdir)
    p = subprocess.Popen('make', cwd=workdir)
    print p.wait()

