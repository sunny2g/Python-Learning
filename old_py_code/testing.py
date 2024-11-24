
1+1
import pandas as pd 

def drop_first_last(data):
    data='sunny'
    a,b,c,d,e=data
    first, *middle, last = data
    print(first,*middle)
drop_first_last(data)

record = ('Sun','sun@gmail.com',123,456)
name,email,*numbers=record
numbers

records = [
    ('foo',1,2),
    ('bar','hello'),
    ('foo',3,4),
]

def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar',s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)    

    
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname,*fields,homedir,sh=line.split(':')
uname
homedir
sh
fields


from collections import deque
lines = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
def search(lines,pattern,history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if '2' in line:
            yield line,previous_lines
        previous_lines.append(line)


