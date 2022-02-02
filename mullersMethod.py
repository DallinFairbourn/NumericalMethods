#!/usr/bin/env python
# coding: utf-8

# In[97]:


import math

def mullers(xr,h,tolerance,maxit,f):
    x2 = xr
    x1 = xr + (h * xr)
    x0 = xr - (h * xr)
    success = False
    for n in range(maxit):
        fx0 = f(x0)
        fx1 = f(x1)
        fx2 = f(x2)
        h0 = x1 - x0
        h1 = x2 - x1
        d0 = (fx1 - fx0) / h0
        d1 = (fx2 - fx1) / h1
        a = (d1 - d0) / (h1 + h0)
        b = (a * h1) + d1
        c = fx2
        rad = math.sqrt(b*b - 4*a*c)
        if abs(b + rad) > abs(b - rad):
            den = b + rad
        else:
            den = b - rad
        dxr = (-2*c) / den
        xr = x2 + dxr
        x0 = x1
        x1 = x2
        x2 = xr
        if abs(dxr) < abs(tolerance*xr):
            success = True
            break
    return (xr,success)


# In[98]:


def func(x):
    return x**3-13*x-12


# In[99]:


mullers(-2, 0.1, 0.01, 3, func)


# In[47]:




