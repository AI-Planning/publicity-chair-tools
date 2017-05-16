
import os, time, shutil, glob

def html_files():
    return glob.glob('../*.html')

def backup():
    fid = str(int(time.time()))
    os.mkdir(os.path.join('backup', fid))
    for f in html_files():
        shutil.copy(f, os.path.join('backup', fid))
