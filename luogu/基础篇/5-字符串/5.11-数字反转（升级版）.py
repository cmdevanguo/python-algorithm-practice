s = input()

if '.' in s:
    a, b = s.split('.')
    a = a[::-1].lstrip('0')
    b = b[::-1].rstrip('0')
    if a == '':
        a = '0'
    if b == '':
        b = '0'
    print(a + '.' + b)

elif '/' in s:
    a, b = s.split('/')
    a = a[::-1].lstrip('0')
    b = b[::-1].lstrip('0')
    if a == '':
        a = '0'
    if b == '':
        b = '0'
    print(a + '/' + b)

elif '%' in s:
    a = s[:-1]
    a = a[::-1].lstrip('0')
    if a == '':
        a = '0'
    print(a + '%')

else:
    s = s[::-1].lstrip('0')
    if s == '':
        s = '0'
    print(s)