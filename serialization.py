import pickle
data1=[{'a':'A', 'b':2, 'c':3.0}] 
data1_string=pickle.dumps(data1) 
data2=pickle.loads(data1_string) 
print ('Equal', (data1==data2))