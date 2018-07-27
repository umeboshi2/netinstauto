import os
import argparse
import subprocess

from ..util import extract_iso, extract_bootblock

from ..preseeder import get_template

netinst_url = 'https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/9.5.0+nonfree/amd64/iso-cd/firmware-9.5.0-amd64-netinst.iso' # noqa


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
    return 0


parser = argparse.ArgumentParser()
parser.add_argument('--url', default=netinst_url)
args = parser.parse_args()
