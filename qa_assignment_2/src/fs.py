class Node:
  ext = '.node'
  parent = None

  def __init__(self, name):
    self.name = name

class Directory(Node):
  ext = '/'
  DIR_MAX_ELEMS = 8
  files = []

  def __init__(self, name, files):
    self.name = name
    self.files = files.copy()

  def add(self, node):
    if (len(self.files) < self.DIR_MAX_ELEMS):
      self.files.append(node)
      node.parent = self
      return True
    elif (len(self.files) == self.DIR_MAX_ELEMS):
      print('Error: Folder size reached maximum capacity')
      return False
    else: 
      return False

  def delete(self, node):
    if (node in self.files):
      self.files.remove(node)
      return True
    else:
      print(f'Error: No such file was found inside the {self.name}/')
      return False

  def move(self, node, destination):
    if (destination.add(node)):
      self.delete(node)
      return True
    elif (type(destination).__name__ != 'Directory'):
      print('Error: Destination should only be a Directory, not any other type')
      return False
    else:
      print('Error: Could not make a copy of a file to move it')
      return False

  def get_file_by_name(self, name, ext):
    for x in self.files:
      if (x.ext == '/'):
        res = x.get_file_by_name(name, ext)
        if (res != False):
          return res
      if (x.name == name and x.ext == ext):
        return x
    return False

  def list_dir(self):
    for x in self.files:
      print(f'{x.name}{x.ext}')

  def list_subdir(self, level = 0):
    for x in self.files:
      print(level * '| ' + f'{x.name}{x.ext}')
      if (type(x).__name__ == 'Directory'):
        x.list_subdir(level + 1)

        


class Binary(Node):
  ext = '.bin'
  contents = ''

  def __init__(self, name, contents):
    self.name = name
    self.contents = contents

  def read_file(self):
    return f'{self.contents}'



class Log(Node):
  ext = '.log'
  contents = ''

  def __init__(self, name, contents):
    self.name = name
    self.contents = contents

  def read_file(self):
    return f'{self.contents}'
    # return f'{self.name}{self.ext}\n{self.contents}'

  def append_line(self, line):
    self.contents += line



class Buffer(Node):
  ext = '.buf'
  MAX_BUF_FILE_SIZE = 8
  queue = []

  def __init__(self, name, files):
    self.name = name
    self.queue = files.copy()

  def push(self, elem):
    if(len(self.queue) == self.MAX_BUF_FILE_SIZE):
      print("Error: Buffer size reached maximum capacity")
      return False
    elif(len(self.queue) < self.MAX_BUF_FILE_SIZE):
      self.queue.append(elem)
      return True
    else:
      print("Error: Buffer is broken")
      return False

  def consume(self):
    if(len(self.queue) == 0):
      print("Warning: Buffer is empty already")
      return False
    elif(len(self.queue) > 0):
      self.queue.pop()
      return True
    else:
      print("Error: Something is very wrong with buffer")
      return False