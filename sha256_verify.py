import hashlib
import argparse
import re

parser = argparse.ArgumentParser(description='Verify a File Hash(SHA-256).',usage='%(prog)s hash\n\nExample: %(prog)s 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
parser.add_argument('HashValue', metavar="hash", type=str, nargs=1,
                    help='Enter the SHA256 hash of the file')
args = parser.parse_args()
clean = re.sub('\W+','', args.HashValue[0])
if (len(clean)==64):
    sample = clean
   #print(sample)
else:
    print("Invalid Hash!")
