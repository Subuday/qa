import sys
sys.path.append('../')
from fs import Log, Binary, Directory, Buffer

def dir1():
  dir1 = Directory('dir', [])
  return dir1


def test_add(dir1):
  log1 = Log('log1', 'logged')
  assert(dir1.add(log1))


def test_contains(dir1):
  log1 = Log('log1', 'logged')
  bin1 = Binary('bin1', 'pretend its bin')

  dir2 = Directory('dir2', [])

  dir2.add(log1)
  dir1.add(bin1)
  dir1.add(dir2)

  assert(dir1.get_file_by_name('log1', '.log') == log1)
  assert(dir1.get_file_by_name('bin1', '.bin') == bin1)


def test_delete(dir1):
  log1 = Log('log1', 'logged')
  bin1 = Binary('bin1', 'pretend its bin')

  dir2 = Directory('dir2', [])

  dir2.add(log1)
  dir1.add(bin1)
  dir1.add(dir2)

  assert(dir1.delete(log1) == False)
  assert(dir1.delete(bin1))
  assert(dir1.delete(dir2))


def test_move(dir1):
  log1 = Log('log1', 'logged')
  bin1 = Binary('bin1', 'pretend its bin')

  dir2 = Directory('dir2', [])
  dir3 = Directory('dir3', [])

  dir2.add(log1)
  dir3.add(bin1)
  dir1.add(dir2)
  dir1.add(dir3)

  assert(dir1.get_file_by_name('log1', '.log') == log1)
  assert(dir1.get_file_by_name('bin1', '.bin') == bin1)

  assert(dir2.move(log1, dir3))
  assert(dir3.get_file_by_name('log1', '.log') == log1)

  assert(dir3.move(log1, bin1) == False)


def test_size(dir1):
  log1 = Log('log1', 'logged')
  log2 = Log('log2', 'logged')
  log3 = Log('log3', 'logged')

  buf1 = Buffer('buf1', ['aa', 'ab'])
  buf2 = Buffer('buf2', ['aa', 'ab'])
  buf3 = Buffer('buf3', ['aa', 'ab'])

  bin1 = Binary('bin1', 'pretend its bin')
  bin2 = Binary('bin2', 'pretend its bin')
  bin3 = Binary('bin3', 'pretend its bin')

  subdir1 = Directory('subdir1', [])
  subdir2 = Directory('subdir2', [])
  subsubdir1 = Directory('subsubdir1', [])

  dir1.add(log1)
  dir1.add(log2)
  dir1.add(log3)
  dir1.add(bin1)
  dir1.add(bin2)
  dir1.add(bin3)
  dir1.add(subdir1)
  dir1.add(subdir2)

  assert(dir1.add(buf1) == False)
  assert(subdir1.add(subsubdir1))
  subsubdir1.add(buf1)
  subdir1.add(buf2)
  subdir2.add(buf3)

  dir1.list_subdir()
  
test_add(dir1())
test_contains(dir1())
test_delete(dir1())
#returns error no such file was found
test_move(dir1())
#returns errors about Directory type and maximum capacity
test_size(dir1())