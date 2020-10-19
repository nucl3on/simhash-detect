import re
import hashlib
import argparse
from simhash import Simhash

parser = argparse.ArgumentParser(description='Calculate a SIMHASH value for a file. -nucl3on',usage='%(prog)s file-location\n\nExample: %(prog)s /home/user/Documents/myfile.doc')
parser.add_argument('FileLocation', metavar="location", type=str, nargs=1,
                    help='Enter the location of the file')
args = parser.parse_args()
# need to add path regex to clean user input.
clean = args.FileLocation[0]

def get_features(s):
    width = 3
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

file = clean
try:
    with open(file) as chunk:
        bytes = chunk.read()
except:
    print ("\nFile Not Found/Access Error!")
    print ("Check your file name/location again.\n")
else:
    final = Simhash(get_features(bytes)).value
    print (final)
