# simhash-detect
Detecting similar text files by calculating distance using simhash algorithm.

Current Limitations:
- Only text data can be processed (UTF-8) (.txt)
- Input File Size < 20 MB


# Usage:
- python3 simhash-detect.py  location/filename1.txt  location/filename2.txt

For Usage Help Run,
- python3 simhash-detect.py  --help

# Sample Output:

File1 hash.VALUE: 11859362079583617622

File2 hash.VALUE: 9663724769906510421

DISTANCE: 18 




- Lesser distance value >> more similarity b/w files.
- If the distance is 0, then the files are identical.
