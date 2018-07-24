import argparse
import subprocess

necessary_binaries = ['xorriso', 'bsdtar', 'wget',
                      'chmod']

optional_binaries = ['convert', 'mogrify']

netinst_url = 'https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/9.5.0+nonfree/amd64/iso-cd/firmware-9.5.0-amd64-netinst.iso' # noqa


def which(binary):
    return subprocess.check_call(['which', binary], stdout=subprocess.DEVNULL)


def main():
    reqs = True
    opts = True
    for binary in necessary_binaries:
        try:
            which(binary)
        except subprocess.CalledProcessError:
            print("ERROR {} not found.".format(binary))
            reqs = False
            continue
        print("Found {}.".format(binary))
    for binary in optional_binaries:
        try:
            which(binary)
        except subprocess.CalledProcessError:
            print("WARNING {} not found.".format(binary))
            opts = False
            continue
        print("Found {}.".format(binary))
    if reqs:
        print("All required commands available.")
    if opts:
        print("All optional commands available.")
    return 0


parser = argparse.ArgumentParser()
args = parser.parse_args()
