# StringIO顾名思义就是在内存中读写str。
from io import StringIO
f = StringIO()
f.write('hbb')
print(f.getvalue())  # getvalue()方法用于获得写入后的str
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO
from io import BytesIO
f1 = BytesIO()
f1.write('好爸爸'.encode('utf-8'))
print(f1.getvalue())  # b'\xe5\xa5\xbd\xe7\x88\xb8\xe7\x88\xb8'