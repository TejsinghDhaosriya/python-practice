def a(x, y):
    print (x, y)
def b(function, *args, **kwargs):
    function(*args, **kwargs)
b(a, 'hello', 'guvi',name='tek',worl='indore')