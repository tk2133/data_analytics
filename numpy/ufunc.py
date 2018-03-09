#coding:utf-8
import numpy as np
np.version.full_version
%timeit

test = np.random.random(100).reshape(5,20)
test.shape
a = np.arange(8)
b = np.arange(7)
a
np.add(a,a)
np.square(a)

a*a
%%timeit
np.add.reduce(test,axis=0)
%%timeit
np.sum(test)


a = np.random.random(8)
b = np.random.random(8)
ta = np.array([[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]])

ta[0,:]
tb = np.array([[3,2,3],[1,1,1],[6,6,6]])
ta.shape
np.divide(ta,tb, axis=1)
np.maximum(ta,tb)
np.add.accumulate(tb,axis=1)
np.add.reduce(tb,axis=1)

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
c = np.add.outer(a,b)
c.shape
c

a = np.arange(8)
np.add.reduce(a)
