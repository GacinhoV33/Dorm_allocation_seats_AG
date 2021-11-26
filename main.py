#!/usr/bin/python
# -*- coding: utf-8 -*-
""" IMPORT FILES"""
from Student import Student

"""IMPORT LIBRARIES"""
import pandas as pd
import numpy as np
from Dorm import Dorm, Room, Rooms
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
    test_population = Population(200, Rooms)
    test_population.initialize_population()
    """ ETAP 3 - Przypisanie pokoji do instancji klasy Student"""
    # TODO

