list =['guvi','learning','is','awesome','asla']

def foo(x):
    print (x*3)

def mymap(fun,list):
    for item in list:
        fun(item)

mymap(foo,list)