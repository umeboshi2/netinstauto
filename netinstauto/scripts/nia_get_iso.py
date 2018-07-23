import os
import argparse
import subprocess


netinst_url = 'https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/9.5.0+nonfree/amd64/iso-cd/firmware-9.5.0-amd64-netinst.iso' # noqa


def extract_iso(filename):
    working_dir = 'cd'
    if not os.path.isdir(working_dir):
        os.mkdir(working_dir)
    print("Extracting {} to {}.".format(filename, working_dir))
    cmd = ['bsdtar', '-C', working_dir, '-xf', filename]
    subprocess.check_call(cmd)
    cmd = ['chmod', '-R', '+w', working_dir]
    subprocess.check_call(cmd)
    print("Files in {} set to writable".format(working_dir))
    print("Netinst cd extracted to {}.".format(working_dir))


def extract_bootblock(filename):
    print("Extracting boot block from {}.".format(filename))
    binfilename = "isohdpfx.bin"
    cmd = ['dd', 'if={}'.format(filename), "of={}".format(binfilename),
           'bs=1', 'count=432']
    subprocess.check_call(cmd)
    print("{} extracted from {}.".format(binfilename, filename))


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
    create_new_iso('test.iso')
    return 0


parser = argparse.ArgumentParser()
parser.add_argument('--url', default=netinst_url)
args = parser.parse_args()
