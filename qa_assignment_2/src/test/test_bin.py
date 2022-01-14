import sys
sys.path.append('../')
from fs import Binary

def bin1():
  bin1 = Binary('binary', 'bin')
  return bin1


def test_readfile(bin1):
  bin1_contents = bin1.read_file()
  assert bin1_contents == 'bin'
  
test_readfile(bin1())