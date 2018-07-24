import os
import argparse
import subprocess
import pkg_resources

from ..util import set_writable_recursive
from ..util import extract_iso, extract_bootblock

from ..preseeder import get_template

netinst_url = 'https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/9.5.0+nonfree/amd64/iso-cd/firmware-9.5.0-amd64-netinst.iso' # noqa


    


def create_new_iso(filename, working_dir='cd',
                   binfilename='isohdpfx.bin'):
    cmd = ['chmod', '-R', '-w', working_dir]
    subprocess.check_call(cmd)
    cmd = ['xorriso', '-as', 'mkisofs', '-o', filename,
           '-isohybrid-mbr', binfilename, '-c',
           'isolinux/boot.cat', '-b', 'isolinux/isolinux.bin',
           '-no-emul-boot', '-boot-load-size', '4',
           '-boot-info-table', './{}'.format(working_dir)]
    subprocess.check_call(cmd)



def main():
    url = args.url
    filename = os.path.basename(args.url)
    if not os.path.isfile(filename):
        print("Downloading {}.".format(filename))
        cmd = ['wget', url]
        subprocess.check_call(cmd)
    else:
        print("{} is present.".format(filename))
    extract_iso(filename)
    extract_bootblock(filename)
    get_template()
    # create_new_iso('test.iso')
    return 0


parser = argparse.ArgumentParser()
parser.add_argument('--url', default=netinst_url)
args = parser.parse_args()
