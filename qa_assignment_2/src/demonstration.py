from fs import Log, Binary, Directory, Buffer

def peek_changes(fs):
  fs.list_subdir()
  print ('')



log1 = Log('log_1', "Ping 1")
log2 = Log('log_2', "Ping 2")
log_sub_1 = Log('logs', "Ping-ping 1")

buf1 = Buffer('buf_1', [])

bin1 = Binary('bin_1', 'exec 1')
bin2 = Binary('bin_2', 'exec 2')
bin_sub_1 = Binary('bins_1', 'exec-exec 1')
bin_sub_2 = Binary('bins_2', 'exec-exec 2')


fs = Directory('.', [])
sub_dir_2 = Directory('sub_dir_2', [bin_sub_1, bin_sub_2])
sub_dir_1 = Directory('sub_dir_1', [sub_dir_2])
dir1 = Directory('bins', [bin1, bin2])
dir2 = Directory('logs', [log1, log2])
dir3 = Directory('bufs', [buf1])
dir4 = Directory('misc', [sub_dir_1])


fs.add(dir1)
fs.add(dir2)
fs.add(dir3)
fs.add(dir4)


#if all files added
peek_changes(fs)

#deleting file
dir1.delete(bin1)

#log append and read test
log2.append_line(' Beep')
print(log2.read_file())

#deleting file
dir2.delete(log2)

#moving files
dir2.move(log1, sub_dir_1)

#deleting whole folder
fs.delete(dir1)

#moving folder
sub_dir_1.move(sub_dir_2, dir2)
test = fs.get_file_by_name('bins_1', '.bin')
print(test.name)

#prevent empty already
buf1.push('0A')
buf1.push('AD')
buf1.push('B4')
buf1.push('CC')
buf1.consume()
