#!/usr/bin/python
# -*- coding: utf-8 -*-
""" IMPORT FILES"""
from plots import show_best_score, show_score_individual, show_frequency_Individual
from Dorm import Dorm
from generate_people import read_from_excel, check_best_in_excel
from Population import Population
from time import time

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
    # ppl = generate_random_people(10010
    path_excel = "Data/Test_december19.xls"
    ppl = read_from_excel(path_excel)
    """ETAP 1 - Stworzenie Akademika"""
    Dorm_TEST = Dorm("Test_dorm", n_floors=5, n_rooms=4,  ppl=ppl)
    """ ETAP 2 - Stworzenie pierwszej populacji """
    test_population = Population(10, 100, ppl, Dorm_TEST, 200)
    # check_best_in_excel(test_population.best_solution.score, path_excel) #TODO
    """ ETAP 3 - Przypisanie pokoji do instancji klasy Student"""
    """TEST INDIVIDUAL"""
    # for individual in test_population.Individual_lst:
    #     individual.check_correctness()

    # test_population.print_pop()
    # test_population.cross_population()
    # test_population.print_pop()
    st = time()
    test_population.Genetic_Algorithm()
    end = time()
    print(f"Simulation took {end - st} seconds.")
    print(test_population.Individual_lst[0].mutation_lst)
    # print(test_population.Individual_lst[0].chose_list)
    # print(test_population.Individual_lst[9].n_of_mutations)
    show_best_score(test_population.best_solutions_lst)
    show_score_individual(test_population.Individual_lst[0].score_lst, test_population.Individual_lst[0].mutation_lst)
    # show_frequency_Individual(test_population.Individual_lst[4].chose_list)
    check_best_in_excel(test_population.best_solution.score, 'Data/Test_december19.xls')
    # test_population.mutation_swap(test_population.Individual_lst[0], 1)
    # print(test_population.best_solution.score)
    # test_population.print_pop()
    # test_population.rullet_selection()
    # print(test_population.best_solution.score)
    # test_population.Genetic_Algortihm()


