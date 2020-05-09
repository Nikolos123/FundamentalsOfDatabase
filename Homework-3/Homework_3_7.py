def my_func(a):
    print(a[:1].upper()+a[1:])
a = 'asdsdFsdaeqwe'
my_func(a)

print('*'*50)

print((lambda a: a[:1].upper()+a[1:])(a))
