import os
import sys
from .reader import READER_CLASS
from .writer import WRITER_CLASS

DEFAULT_SUFFIX = ".xlsx"
VALID_SUFFIX = [".txt", ".xlsx"]

def is_valid(filename):
    if isinstance(filename, str) and len(filename) > 0 and not filename.isspace():
        if not os.path.exists(filename):
            raise ValueError("This file is not exist %s." % filename)
    else:
        raise ValueError("This is not a valid parameter %s." % filename)

def create_instance_by_classname(classname, *args):
    module = sys.modules["__main__"]
    return getattr(module, classname)(args)

def check_suffix(filename, dot_index):
    suffix = filename[dot_index:len(filename)].strip().lower()
    if not suffix in VALID_SUFFIX: raise ValueError()
    return suffix

def get_reader(filename):
    dot_index = filename.find(".")
    if dot_index < 0:
        raise ValueError("Your filename %s is invalid." % filename)

    try:
        suffix = check_suffix(filename, dot_index)
    except ValueError:
        print("Your filename %s is invalid." % filename)

    reader_classname = READER_CLASS[suffix]
    return create_instance_by_classname(reader_classname, filename)

def get_writer(dest_filename):
    dot_index = dest_filename.find(".")
    if dot_index < 0:
        dest_filename = dest_filename + DEFAULT_SUFFIX
        dot_index = dest_filename.find(".")
    try:
        suffix = check_suffix(dest_filename, dot_index)
    except ValueError:
        print("Your destination filename %s is invalid." % dest_filename)

    writer_classname = WRITER_CLASS[suffix]
    return create_instance_by_classname(writer_classname, dest_filename)
