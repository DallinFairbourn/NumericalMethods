#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math

def taylor_series_approx_of_cos(x,n):
    y = 0
    i = 0
    a = 0
    while i <= n:
        fac = math.factorial(i)
        if i == 0 or i % 4 == 0:
            ith_deriv = math.cos(a)
        elif i == 1 or i % 5 == 0:
            ith_deriv = -math.sin(a)
        elif i == 2 or i % 6 == 0:
            ith_deriv = -math.cos(a)
        elif i == 3 or i % 7 == 0:
            ith_deriv = math.sin(a)
        y += ith_deriv * (x - a) ** i / fac
        i += 1
    return y

taylor_series_approx_of_cos(math.pi, 8)


# In[32]:


import sympy as sym

a = Symbol('a')

sym.diff(cos(a),a,1)


# In[ ]:




