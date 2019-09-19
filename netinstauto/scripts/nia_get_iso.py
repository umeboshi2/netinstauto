import os
import argparse
import requests

from ..util import extract_iso, extract_bootblock
from ..util import check_file_sha256, download_file


url_root = "https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/{version}/{arch}/iso-cd" # noqa


def get_remote_checksum(urlroot):
    sha_url = os.path.join(urlroot, 'SHA256SUMS')
    res = requests.get(sha_url)
    line = res.content.decode().strip()
    sha256, filename = line.split()
    return sha256, filename


def main():
    url = args.url
    if args.filename is None:
        if url is None:
            dirname = url_root.format(version=args.debversion, arch=args.arch)
            sha256, filename = get_remote_checksum(dirname)
            url = os.path.join(dirname, filename)
        else:
            filename = os.path.basename(args.url)
            sha256, filename = get_remote_checksum(os.path.dirname(args.url))
    else:
        filename = args.filename
    if not os.path.isfile(filename):
        print("Downloading {}.".format(filename))
        download_file(url, filename)
    if not os.path.isfile(filename):
        raise RuntimeError("{} is absent!".format(filename))
    else:
        if args.filename is None:
            if check_file_sha256(filename, sha256):
                print("{} is present.".format(filename))
            else:
                raise RuntimeError("Bad iso checksum for {}".format(filename))
    extract_iso(filename)
    extract_bootblock(filename)
    return 0


parser = argparse.ArgumentParser()
parser.add_argument('--url', default=None)
parser.add_argument('--debversion', default='current')
parser.add_argument('--arch', default='amd64')
parser.add_argument('--filename', default=None)
args = parser.parse_args()
