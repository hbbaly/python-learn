# 文件读取
# 传入标识符'w'或者'wb'表示写文本文件或写二进制文件, r表示读取
try:
  f = open('../demo1/demo1.py','r')  # open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在：
  f.read()  # 调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
finally:
  if f:
    f.close() # close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：


# try 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：

with open('../demo1/demo1.py', 'r') as f:
    print(f.read())

# 可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：

for line in f.readlines():
    print(line.strip())