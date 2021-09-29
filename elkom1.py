# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 09:26:07 2021

@author: tamaraa
"""

from math import sqrt
formula = input('Sisi mana yang ingin anda hitung = ')

if formula =='c':
    sisiA = int(input('Masukkan panjang sisi a = '))
    sisiB = int(input('Masukkan panjang sisi b = '))
    
    sisiC = sqrt(sisiA*sisiA + sisiB*sisiB)
    print('Panjang sisi c adalah', sisiC)

elif formula =='a':
    sisiC = int(input('Masukkan panjang sisi c = '))
    sisiB = int(input('Masukkan panjang sisi b = '))
    
    sisiA = sqrt(sisiC*sisiC - sisiB*sisiB)
    print('Panjang sisi a adalah', sisiA)
    
elif formula =='b':
    sisiC = int(input('Masukkan panjang sisi c = '))
    sisiA = int(input('Masukkan panjang sisi a = '))
    
    sisiB = sqrt(sisiC*sisiC - sisiA*sisiA)
    print('Panjang sisi b adalah', sisiB)
    
else:
    print('Input Salah')

