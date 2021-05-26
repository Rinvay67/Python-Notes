# 正则表达式

## 1. 文本查找

```python
def find_in_hello(f_name):
    f = open(f_name)
    for line in f:
        if line.startswith('hello') and line[:-1].endswith('hello'):
            print(line)
    f.close()
```

```python
s = 'hello1 python hello2 java jack php hello apple hello_world'
print(s.find('11'))
print(s.startswith('hello'))
pattern = re.compile(r'hello')
ma = pattern.match(s)
print(ma.group())
print(ma.span())
print(ma.string)
print(ma.re)
# -1
# True
# hello
# (0, 5)
# hello1 python hello2 java jack php hello apple hello_world
# re.compile('hello')
```

## 2. 大小写

```python
s2 = 'Hello World'
pattern = re.compile(r'hello', re.IGNORECASE)
ma = pattern.match(s2)
print(ma.group())
# Hello
```

## 3. group

```python
s = 'hello1 python hello2 java jack php hello apple hello_world'
pattern = re.compile(r'(hello)')
ma = pattern.match(s)
print(ma.groups())
print(ma.group(0))
print(ma.group(1))
# ('hello',)
# hello
# hello
```

## 4. match

```python
s = 'hello python hello2 java jack php hello apple hello_world'
ma = re.match(r'hello', s)
print(ma.group())
# hello
```

## 5. pattern

```python
ma = re.match(r'{[a-zA-Z0-9]{5}}', '{demo9}')
ma = re.match(r'{[\w]{5}}', '{demo9}')
ma = re.match(r'\[[\w]{5}\]', '[demo9]')
ma = re.match(r'\[[A-Z][\w]*\]', '[Demo9]')
```

```python
ma = re.match(r'^[\w]{4,10}@163.com$', 'imooc@163.com')
ma = re.match(r'\Aimooc[\w]*', 'imoocpython')
ma = re.match(r'[\w]*.imooc\Z', 'java.imooc')
```

```python
ma = re.match(r'abc|def', 'def')
ma = re.match(r'[1-9]?\d$|100', '19')
ma = re.match(r'[\w]{4,6}@(163|126|sina).com', 'imooc@sina.com')
ma = re.match(r'<(\w+>)', '<book>')
ma = re.match(r'<(\w+>)\1', '<book>book>')
```

```python
# 匹配一个有效的xml标签
ma = re.match(r'<(\w+>)\w+</\1', '<book>python</book>')
```

```python
# 给分组起一个别名 并且使用分组的别名
ma = re.match(r'<(?P<mark>\w+>)\w+</(?P=mark)', '<book>python</book>')
```

## 6. search

```python
str1 = 'imooc video num = 1000'
print(str1.find('1000'))
# 18
```

```python
res = re.search(r'\d+', str1)
print(res.group())
# 1000
```

## 7. split

```python
str2 = 'imooc:C C++ Java Python,C#'
res = re.split(r':| |,+', str2)
print(res)
# ['imooc', 'C', 'C++', 'Java', 'Python', 'C#']
```

## 8. findall

```python
str3 = 'banana'
res = re.findall(r'a|b|c*', str3)
print(res)
# ['b', 'a', '', 'a', '', 'a', '']
```

## 9. sub

```python
str4 = 'mobile phone'
res = re.sub(r'\w{6}\s', 'i', str4)
print(res)
# iphone
```
