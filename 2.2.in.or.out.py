# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:18:13 2024

@author: baaij
"""
n,o=input().split()
noord= float(n)
oost = float(o)
no=52+5/60+28/3600
so=52+4/60+52/3600
we=5+9/60+49/3600
ea=5+11/60+5/3600
if so<=noord<=no and we<=oost<=ea:
    print('inside')
else: 
    print('outside')