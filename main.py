#!/usr/bin/python
# -*- coding: utf-8 -*-
""" IMPORT FILES"""
from Student import Student

"""IMPORT LIBRARIES"""
import pandas as pd
import numpy as np
# from Dorm import
from Individual import Individual, Dorm, Room, Rooms
from generate_people import ppl
from Population import Population
""" 'P' is reserved for whole kind of probabilities"""


"""
PRECONDITIONS:


N - Number of people willing live in dorm (400)

D - Total number of places in dorm (100)
D_2 - Total number of places in dorm (only two-man rooms)
D_3 - Total number of places in dorm (only three-man rooms)
D_2 + D_3 = D (Algorithm should try find proportional amount of boys ang girls)

GIRLS CANNOT LIVE WITH BOYS 

"""

if __name__ == "__main__":
    """ETAP 0 - stworzenie niezbędnych struktur i danych"""

    """ETAP 1 - Stworzenie Akademika"""
    Dorm_TEST = Dorm("Test_dorm", Rooms, n_floors=5)
    """ ETAP 2 - Stworzenie pierwszej populacji """
    test_population = Population(10, 100, ppl)
    """ ETAP 3 - Przypisanie pokoji do instancji klasy Student"""

    """TEST INDIVIDUAL"""
    if test_population.Individual_lst[0].arr_bin.shape[0] != 100:
        print("Wrong Individual test 1")

    f = 0

    print(test_population.Individual_lst[0].arr_bin)
    for room in Rooms:

        c = 0
        for i in test_population.Individual_lst[0].arr_bin:
            if int(room.number) == int(i):
                c += 1
        if room.capacity != c:
            f += 1
            print(f"Wrong Individual test 2 -{f}")

    # TODO

