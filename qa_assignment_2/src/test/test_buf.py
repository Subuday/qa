import sys
sys.path.append('../')
from fs import Buffer

def buf1():
  buf1 = Buffer('buffer', [])
  return buf1


def test_push(buf1):
  elem01 = '00'
  assert(buf1.push(elem01))


def test_maximum(buf1):
  elem_arr =  ['aa', 'ab', 'ac', 'ad', 'ae', 'af', 'b0', 'b1']
  elem01 = '00'
  buf1 = Buffer('buffer2', elem_arr)

  assert(buf1.push(elem01) == False)


def test_consume(buf1):
  elem01 = '00'
  buf1.push(elem01)
  assert(buf1.consume())
  assert(buf1.consume() == False)
  
test_push(buf1())
test_maximum(buf1())
test_consume(buf1())