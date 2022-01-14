import sys
sys.path.append('../')
from fs import Log

test_string = 'Ping ping...'

def log1():
  log1 = Log('log1', test_string)
  return log1


def test_readfile(log1):
  log1_contents = log1.read_file()

  assert log1_contents == test_string


def test_appendline(log1):
  log1.append_line(' Beep-boop...')
  log1_contents = log1.read_file()
  
  assert log1_contents == test_string + ' Beep-boop...'

test_readfile(log1())
test_appendline(log1())