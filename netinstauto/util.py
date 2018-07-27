import os
import subprocess


def set_writable_recursive(working_dir):
    cmd = ['chmod', '-R', '+w', working_dir]
    subprocess.check_call(cmd)
    print("Files in {} set to writable".format(working_dir))


def extract_iso(filename, working_dir='netinst'):
    if not os.path.isdir(working_dir):
        os.mkdir(working_dir)
    else:
        set_writable_recursive(working_dir)
    print("Extracting {} to {}.".format(filename, working_dir))
    cmd = ['bsdtar', '-C', working_dir, '-xf', filename]
    subprocess.check_call(cmd)
    set_writable_recursive(working_dir)
    print("Netinst cd extracted to {}.".format(working_dir))


def extract_bootblock(filename):
    print("Extracting boot block from {}.".format(filename))
    binfilename = "isohdpfx.bin"
    cmd = ['dd', 'if={}'.format(filename), "of={}".format(binfilename),
           'bs=1', 'count=432']
    subprocess.check_call(cmd)
    print("{} extracted from {}.".format(binfilename, filename))


def create_new_iso(filename, working_dir='netinst',
                   binfilename='isohdpfx.bin'):
    cmd = ['chmod', '-R', '-w', working_dir]
    subprocess.check_call(cmd)
    cmd = ['xorriso', '-as', 'mkisofs', '-o', filename,
           '-isohybrid-mbr', binfilename, '-c',
           'isolinux/boot.cat', '-b', 'isolinux/isolinux.bin',
           '-no-emul-boot', '-boot-load-size', '4',
           '-boot-info-table', './{}'.format(working_dir)]
    subprocess.check_call(cmd)
