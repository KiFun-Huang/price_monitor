from utils.thief import *
from utils.reader import TxtReader,ExcelReader
from utils.writer import TxtWriter,ExcelWriter
from utils.util import is_valid, get_reader, get_writer
import sys

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Please enter two file names")
        print("The first file gets the URL.\nThe second file saves the results.")
        exit(1)

    
    filename = sys.argv[2]
    is_valid(filename)
    reader = get_reader(filename)

    dest_filename = sys.argv[3]
    writer = get_writer(dest_filename)

    if sys.argv[1] == "lsdj":
        thief = SimpleThief(reader=reader, writer=writer)
        thief.handle()
    elif sys.argv[1] == "gwd":
        thief = SelenThief(reader=reader, writer=writer)
        thief.handle()
    else:
        print('Parameter error , Now only "lsdj" and "gwd" are supported.')
        print('lsdj: http://p.zwjhl.com')
        print('gwd: https://www.gwdang.com')