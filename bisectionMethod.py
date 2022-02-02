#!/usr/bin/env python
# coding: utf-8

# In[21]:


def bisection(x0, x1, tol, maxit, f):
    f0 = f(x0)
    f1 = f(x1)
    i = 0
    success = False
    for n in range(maxit):
        x2 = (x0 + x1) / 2
        f2 = f(x2)
        if f0 * f2 > 0:
            x0 = x2
            i += 1
        elif f1 * f2 > 0:
            x1 = x2
            i += 1
        if abs(f2) < tol:
            success = True
            break
    return x2, success

def func(x):
    return x*x-4

print(bisection(0.5, 4, 0.01, 12, func))


# In[ ]:




