# simhash-detect
Detecting similar text files by calculating distance using simhash algorithm.

Current Limitations:
- (UTF-8) text can only be processed
- Only text files can be used with the script
- Input File Size < 20 MB


# Usage:
If the files are in the same dir:
- python3 simhash-detect.py file1 file2

Else, specify file path
- python3 simhash-detect.py path/file1 path/file2

For Usage Help Run,
- python3 simhash-detect.py  --help

# Sample Output:

File1 hash.VALUE: 11859362079583617622

File2 hash.VALUE: 9663724769906510421

DISTANCE: 18 




- Lesser distance value means more similarity b/w files.
- If the distance is 0, then the files are identical.
