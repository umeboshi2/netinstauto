import argparse
import subprocess

necessary_binaries = ['xorriso', 'bsdtar', 'wget',
                      'chmod']

netinst_url = 'https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/9.5.0+nonfree/amd64/iso-cd/firmware-9.5.0-amd64-netinst.iso' # noqa


def main():
    for binary in necessary_binaries:
        try:
            subprocess.check_call(['which', binary],
                                  stdout=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            print("ERROR {} not found.".format(binary))
            continue
        print("Found {}.".format(binary))
    return 0


parser = argparse.ArgumentParser()
args = parser.parse_args()
