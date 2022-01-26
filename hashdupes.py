import hashlib
import os

def scan_dirs():
    hashes = {}
    found = []
    basepath = r'd:\dropbox'
    dirs = ['Books', 'Large Books', 'Processed Books']
    for d in dirs:
        files = os.listdir(os.path.join(basepath, d))
        for f in files:
            fullname = os.path.join(basepath, d, f)
            if not os.path.isdir(fullname):
                newhash = gen_hash(fullname)[:16]
                if newhash in hashes:
                    print(f'Duplicate found - {f} -> {hashes[newhash]}')
                    found.append(f'Duplicate found - {f} -> {hashes[newhash]}')
                hashes[newhash] = fullname
    return '\n'.join(found)

def export(outdata):
    with open(r'd:\tmp\hashdupes.txt', 'w') as outfile:
        outfile.write(outdata)

def gen_hash(infile):
    try:
        with open(infile, "rb") as f:
            file_hash = hashlib.blake2b()
            while chunk := f.read(8192):
                file_hash.update(chunk)
        return file_hash.hexdigest()[:16]
    except Exception as err:
        print(err)

def main():
    found = scan_dirs()
    export(found)

if __name__ == '__main__':
    main()
