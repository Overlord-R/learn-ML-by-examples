# -*- coding: utf-8 -*-
"""
Created by : Overlord

"""
import gzip
import os
from six.moves.urllib.request import urlretrieve
import numpy

SOURCE_URL = 'http://yann.lecun.com/exdb/mnist/'

def if_not_downloaded(filename, work_directory):
    if not os.path.exists(work_directory):
        os.mkdir(work_directory)
    filepath =os.path.join(work_directory, filename)
    if not os.path.exists(filepath):
        filepath, _ = urlretrieve(SOURCE_URL + filename, filepath)
        statinfo = os.stat(filepath)
        print('Successfully downloaded', filename, statinfo.st_size, '.bytes')
    return filepath

def _read32(bytestream):
    dt = numpy.dtype(numpy.unint32).newbyteorder('>')
    return numpy.frombuffer(bytestream.read(4), dtype=dt)

def extract_images(filename):
    # 4D [index, y, x, depth]
    print('Extracting', filename)
    with gzip.open(filename) as bytestream:
        magic = _read32(bytestream)