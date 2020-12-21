from utils.thief import *
from utils.reader import TxtReader,ExcelReader
from utils.writer import TxtWriter,ExcelWriter
from utils.util import is_valid, get_reader, get_writer

if __name__ == '__main__':
    filename = input("Please enter your filename: ")
    is_valid(filename)
    reader = get_reader(filename)

    dest_filename = input("Please enter your destination filename you want to save that query results: ")
    writer = get_writer(dest_filename)

    thief = SelenThief(reader=reader, writer=writer)
    thief.handle()
    