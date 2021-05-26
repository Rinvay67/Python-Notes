# 文件读写

## 1. 内置函数

### 1.1. open 函数

```python
f = open('hello.txt')
content = f.read()
print(content)
f.close()
```

```python
f = open('hello.txt')
first_line = f.readline()
print(first_line)
second_line = f.readline()
print(second_line)
f.close()
```

```python
f = open('hello.txt')
lines = f.readlines()
print(lines)
f.close()
```

```python
import io
# 缓冲区大小
print(io.DEFAULT_BUFFER_SIZE)
# 8192
```

### 1.2. 使用迭代器

```python
f = open('hello.txt')
iter_f = iter(f)
lines = ''
for it in iter_f:
    lines += it
f.close()
print(lines)
```

### 1.3. 写文件

```python
f = open('hello.txt', 'w')
f.write('test write ...\n')
f.close()
f = open('hello.txt', 'a')
f.writelines(['a', 'b', 'c', '\n'])
f.writelines(('1', '2', '3', '\n'))
f.close()
f = open('hello.txt', 'r')
print(f.read())
# test write ...
# abc
# 123
f.close()
```

```python
# 写缓存机制
f = open('hello.txt', 'w+')
f.write('test write ...\n')
print('content: ' + f.read())
# content:
f.close()
f = open('hello.txt', 'r')
print('content: ' + f.read())
# content: test write ...
f.close()
```

### 1.4. 读写指针

```python
import os


def cat(path):
    f = open(path, 'r')
    print('content: ' + f.read())
    print(f.fileno())
    f.close()


f = open('hello.txt', 'w+')
f.write('test write ...\n')
f.flush()
f.seek(0, os.SEEK_SET)
print(f.tell())
print('content: ' + f.read())
print(cat(f.name))
f.close()
```

### 1.5. 文件句柄

```python
list_f = []
for i in range(1025):
    list_f.append(open('hello.txt', 'w'))
    print('%d: %d' % (i, list_f[i].fileno()))
```

### 1.6. with 语句

```python
with open('hello.txt', 'r') as f:
    print(f.read())
```

## 2. 文本编码

```python
f = open('hello2.txt', 'w')
s = str('你好\n')
f.write(s)
print(f.encoding)
# cp936
f.close()
```

```python
f = open('hello3.txt', 'w', encoding='utf8')
s = str('你好\n')
f.write(s)
print(f.encoding)
# utf8
f.close()
```

```python
import codecs
f = codecs.open('hello3.txt', 'r', 'utf8')
print(f.encoding)
# utf8
print(f.readlines())
f.close()
```

## 3. os 模块

### 3.1. 文件

```python
import os
fd = os.open('hello4.txt', os.O_CREAT | os.O_RDWR)
os.write(fd, bytes('hello4.txt\n', 'utf-8'))
os.lseek(fd, 0, os.SEEK_SET)
print(os.read(fd, 5))
# b'hello'
os.close(fd)
```

```python
import os
print(os.access('hello4.txt', os.O_RDONLY))
# True
```

### 3.2. 文件夹

```python
import os
if not os.path.exists('dir1'):
    os.mkdir('dir1')
if not os.path.exists('dir1/dir2'):
    os.makedirs('dir1/dir2')
else:
    print(os.listdir('dir1'))
    # ['dir2']
    os.removedirs('dir1/dir2')
```

```python
import os
if not os.path.exists('hello4.txt'):
    hello = os.open('hello4.txt', os.O_CREAT)
else:
    hello = os.open('hello4.txt', os.O_RDONLY)
print(os.path.isdir('hello4.txt'))
print(os.path.isfile('hello4.txt'))
print(os.path.getsize('hello4.txt'))
print(os.path.dirname('hello4.txt'))
print(os.path.basename('hello4.txt'))
print(os.path.abspath('hello4.txt'))
```

## 4. 读写 ini

```python
from configparser import ConfigParser


config = ConfigParser()

config['default'] = {'IP': '192.168.14.2', 'PORT': '6072'}

config['custom'] = {}
config['custom']['user'] = 'admin'
config['custom']['password'] = '123456'

config['define'] = {}
sub_config = config['define']
sub_config['host'] = '192.168.14.2'
sub_config['port'] = '611'

config.add_section('key1')
config.set('key1', 'k1', '123456')
# config.remove_section('key1')
# config.remove_option('key1', 'k1')

with open('config.ini', 'w') as file:
    config.write(file)
```

```python
from configparser import ConfigParser


config = ConfigParser()

config.read('config.ini')
print(config.sections())

options = config.options('custom')
print(options)

value1 = config['custom']['user']
print(value1)
value2 = config.get('custom', 'user')
print(value2)

items = config.items('default')
print(items)

for key in config['default']:
    print(key)
```
