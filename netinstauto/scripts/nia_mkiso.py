import os
import argparse
import subprocess
from io import BytesIO
import yaml

from ..util import set_writable_recursive
from ..util import create_new_iso
from ..preseeder import get_template

_archmap = dict(i386='386', amd64='amd')

def make_preseed_content():
    template = get_template()
    config = yaml.load(open(args.preseed))
    return template.render(**config['preseed_vars'])


def create_preseed_file(filename):
    with open(filename, 'w') as outfile:
        content = make_preseed_content()
        outfile.write(content)


def get_initrd_filename():
    wd = args.working_dir
    arch = _archmap[args.arch]
    dirname = os.path.join(wd, "install.{}".format(arch))
    filename = os.path.join(dirname, "initrd.gz")
    return filename

def update_initrd():
    filename = get_initrd_filename()
    print("filename {}".format(filename))
    if not os.path.isfile(filename):
        raise RuntimeError("initrd not found")
    print("initrd.gz at {}".format(filename))
    cmd = ['gunzip', filename]
    subprocess.check_call(cmd)
    # remove .gz from filename
    unzipped = filename[:-3]
    # add preseed to tar
    cmd = ['cpio', '-H', 'newc', '-o', '-A', '-F', unzipped]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    #proc.stdin.write(make_preseed_content().encode())
    proc.stdin.write('preseed.cfg\n'.encode())
    proc.stdin.close()
    proc.wait()
    cmd = ['gzip', unzipped]
    subprocess.check_call(cmd)

def main():
    set_writable_recursive(args.working_dir)
    preseed_filename = os.path.join(args.working_dir, 'preseed.cfg')
    create_preseed_file(preseed_filename)
    update_initrd()
    create_new_iso('remastered.iso', working_dir=args.working_dir)
    return 0


parser = argparse.ArgumentParser()
parser.add_argument('--working-dir', '-w', default='netinst')
parser.add_argument('--preseed', '-p', default='preseed.yaml')
parser.add_argument('--arch', '-a', default='amd64')
args = parser.parse_args()
