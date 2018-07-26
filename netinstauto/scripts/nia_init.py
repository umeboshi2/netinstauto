import os
import argparse
import subprocess
import pkg_resources

from ..util import set_writable_recursive
from ..util import extract_iso, extract_bootblock

from ..preseeder import get_template

gitignore = """\
/netinst
/*-netinst.iso
/isohdpfx.bin
"""

def git_init():
    if not os.path.isdir('.git'):
        cmd = ['git', 'init']
        subprocess.check_call(cmd)
        with open('.gitignore', 'w') as outfile:
            outfile.write(gitignore)
        cmd = ['git', 'add', '.gitignore']
        subprocess.check_call(cmd)
        cmd = ['git', 'commit', '-m', 'Initial commit.']
        subprocess.check_call(cmd)
        
def main():
    if not os.path.isdir('.git'):
        git_init()
    
    # create_new_iso('test.iso')
    return 0


parser = argparse.ArgumentParser()
args = parser.parse_args()
