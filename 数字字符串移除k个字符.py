#-*-coding=utf-8-*-
#/uer/bin/env python
"�ַ����Ƴ�k���ַ�"

num,k= "5132219",3
size = len(num)
stack = ['0']
for x in range(size):
    while stack[-1] > num[x] and len(stack) + k > x + 1:
        stack.pop()
    stack.append(num[x])
while len(stack) > size - k + 1:
        stack.pop()
print str(int(''.join(stack)))
