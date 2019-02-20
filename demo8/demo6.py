# 正则练习
# someone@gmail.com
# bill.gates@microsoft.com
import re
# a = re.compile(r'(^a-z+._-)@(a-z+.com$)')
A = re.match(r'^([a-z.]+)@([a-z]+.com$)', 'bsomeone@gmail.com').group()
B = re.match(r'^([a-z.]+)@([a-z]+.com$)', 'bill.gates@microsoft.com').group()


def is_has(a):
    if a:
        return a
    else:
        return '不符合'


print(is_has(A))
print(is_has(B))
