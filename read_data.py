#!/usr/bin/python
# -*- coding: utf-8 -*-
from Student import Student
import pandas as pd

data = pd.read_csv('Data/Petenci_test.csv', sep=';')
n_of_students = len(data['Imie'])
all_students = list()

for i in range(0, n_of_students):
    all_students.append(
        Student(data['Imie'][i], data['Nazwisko'][i],
                data['PLEC'][i], data['Odleglosc'][i],
                data['Rok'][i], data['Standard'][i],
                data['PESEL'][i], data['Dochod'][i],
                data['Znajomi_w_pokoju'][i])
    )

