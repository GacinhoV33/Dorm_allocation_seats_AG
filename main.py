#!/usr/bin/python
# -*- coding: utf-8 -*-
""" IMPORT FILES"""
from Student import Student

"""IMPORT LIBRARIES"""
import numpy as np
# from Dorm import
from Individual import Individual, Dorm, Room
from generate_people import generate_random_people
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
    ppl = generate_random_people(100)
    """ETAP 1 - Stworzenie Akademika"""
    Dorm_TEST = Dorm("Test_dorm", n_floors=5, n_rooms=4,  ppl=ppl)
    """ ETAP 2 - Stworzenie pierwszej populacji """
    test_population = Population(10, 100, ppl, Dorm_TEST)
    """ ETAP 3 - Przypisanie pokoji do instancji klasy Student"""
    print(Dorm_TEST)
    """TEST INDIVIDUAL"""
    for individual in test_population.Individual_lst:
        individual.check_correctness()

    test_population.print_pop()

