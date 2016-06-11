import os
import glob

lib_dir = os.path.join(os.path.dirname(__file__), 'lib')
jar_files = [f for f in os.listdir(lib_dir) if f.endswith('.jar')]

try:
    pdfbox_jar = [f for f in jar_files if f.startswith('pdfbox-app')][0]
    pdfbox_jar = os.path.abspath(os.path.join(lib_dir, pdfbox_jar))
except IndexError:
    raise RuntimeError('Could not find suitable pdfbox-app*.jar file')


def pdfbox(command, args):

    cmd = 'java -jar "{}" {} {}'.format(pdfbox_jar, command, ' '.join(args))
    print(cmd)
    print(os.system(cmd))

if __name__ == '__main__':
    pdfbox('OverlayPDF', 
           ['index2.pdf', 'floatable-2.pdf', 'out.pdf'])
