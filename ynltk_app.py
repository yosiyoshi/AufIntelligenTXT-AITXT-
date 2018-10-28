# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 09:51:36 2018

@author: user
"""
from ynltk import Langvowel, OmnibusStem
txt = "Dit is een boek."
l=Langvowel()
s=OmnibusStem()
print(l.langvowel(txt))
print(s.compStemmer("haus","huis"))