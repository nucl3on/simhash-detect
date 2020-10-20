import re
#DEBUG
#import traceback
import argparse
from simhash import Simhash

parser = argparse.ArgumentParser(description='Compare Similarity of Two Docs using Simhash.',usage='%(prog)s file1-location file2-location')
parser.add_argument('File1Location', metavar="location1", type=str, nargs=1, help='Enter the location of the file1')
parser.add_argument('File2Location', metavar="location2", type=str, nargs=1, help='Enter the location of the file2')
args = parser.parse_args()
# need to add regex to clean user input.
clean1 = args.File1Location[0]
clean2 = args.File2Location[0]

def get_features(s):
    width = 3
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

try:
    with open(clean1) as chunk:
        bytes1 = chunk.read()
    with open(clean2) as chunk:
        bytes2 = chunk.read()
except:
    #DEBUG
    #traceback.print_exc()
    print ("\n\nFile Read Error/Not Found!")
    print ("Check your file name/location again \n(or) check for invalid characters/bytes in the file(s).\n")
else:
    hash1 = Simhash(bytes1)
    hash2 = Simhash(bytes2)
    #DEBUG
    #print ("\nFile1 Obj:",hash1)
    #print ("File1 Features:",Simhash(get_features(bytes1)).value)
    #print ("File2 Obj:",hash2)
    #print ("File2 Features:",Simhash(get_features(bytes2)).value)
    print ("\nFile1 hash.VALUE:",hash1.value)
    print ("File2 hash.VALUE:",hash2.value)
    print ("\nDISTANCE:",hash1.distance(hash2),"\n")
