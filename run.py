#!/usr/bin/python
# -*- coding: utf-8 -*-
#!/usr/bin/python
# -*- coding: utf-8 -*-
""" IMPORT FILES"""
from plots import show_best_score, show_score_individual, show_frequency_Individual, show_best_score_iter
from Dorm import Dorm
from generate_people import read_from_excel, check_best_in_excel, generate_random_people
from Population import Population
from time import time
from random import randint
"""
PRECONDITIONS:

N - Number of people willing live in dorm (400)

D - Total number of places in dorm (100)
D_2 - Total number of places in dorm (only two-man rooms)
D_3 - Total number of places in dorm (only three-man rooms)
D_2 + D_3 = D (Algorithm should try find proportional amount of boys ang girls)

"""


def start_simulation(path: str=None, n_of_people: int=None, iteration: int=100, n_of_individuals: int=50, mutation_non_included_probability: float=0.1,
                     mutation_swap_probability: float=0.1, mutation_swap_flag: bool=True, mutation_non_included_flag:bool=True,
                 rullet_selection_flag: bool=True, tournament_selection_flag=False, rank_selection_flag:bool=False, DormType: int=1, info_flag:bool=True):
    if path:
        ppl = read_from_excel(path)
    elif n_of_people:
        ppl = generate_random_people(n_of_people)
    else:
        raise ImportError("Running simulation without parameters")

    if DormType == 1:
        Simulation_Dorm = Dorm("Olimp", n_floors=8, n_rooms=6,  ppl=ppl)
    elif DormType == 2:
        Simulation_Dorm = Dorm("Filutek", n_floors=8, n_rooms=5, ppl=ppl)
    elif DormType == 3:
        Simulation_Dorm = Dorm("Filutek", n_floors=14, n_rooms=10, ppl=ppl)
    elif DormType == 4:
        Simulation_Dorm = Dorm("Random_Dorm", n_floors=randint(3, 10), n_rooms=randint(3, 12), ppl=ppl)
    Simulation_Population = Population(number_of_individuals=n_of_individuals, number_of_students=len(ppl),
                                       ppl=ppl, dorm=Simulation_Dorm, number_of_iterations=iteration,
                                       mutation_non_included_probability=mutation_non_included_probability,
                                       mutation_swap_probability=mutation_swap_probability,
                                       mutation_swap_flag=mutation_swap_flag, mutation_non_included_flag=mutation_non_included_flag,
                                       rullet_selection_flag=rullet_selection_flag, tournament_selection_flag=tournament_selection_flag,
                                       rank_selection_flag=rank_selection_flag, info_flag=info_flag
                                       )
    st = time()
    Simulation_Population.Genetic_Algorithm()
    end = time()
    print(f"Simulation took {end - st} seconds.")
    show_best_score_iter(Simulation_Population.best_solutions_iter, Simulation_Population.number_of_individuals)
    show_best_score(Simulation_Population.best_solutions_lst)
    return Simulation_Population.best_solution


if __name__ == "__main__":
    """ETAP 0 - stworzenie niezbędnych struktur i danych"""
    ppl = generate_random_people(150)
    path_excel = "Data/Test_december19.xls"
    # ppl = read_from_excel(path_excel)
    """ETAP 1 - Stworzenie Akademika"""
    Dorm_TEST = Dorm("Test_dorm", n_floors=5, n_rooms=6,  ppl=ppl)
    """ ETAP 2 - Stworzenie pierwszej populacji """
    test_population = Population(50, 150, ppl, Dorm_TEST, 50)
    # start_simulation(path=None, n_of_people=150, iteration=30, n_of_individuals=25,mutation_non_included_probability=0.1,
    #                  mutation_swap_probability=True, mutation_swap_flag=True, mutation_non_included_flag=True,
    #                  rullet_selection_flag=True, tournament_selection_flag=False, rank_selection_flag=False, DormType=1,
    #                  info_flag=True)

    st = time()
    test_population.Genetic_Algorithm()
    end = time()
    print(f"Simulation took {end - st} seconds.")
    show_best_score(test_population.best_solutions_lst)
    show_score_individual(test_population.Individual_lst[0].score_lst, test_population.Individual_lst[0].mutation_lst)
    show_frequency_Individual(test_population.Individual_lst[4].chose_list)
    show_best_score_iter(test_population.best_solutions_iter, test_population.number_of_individuals)
    # check_best_in_excel(test_population.best_solution.score, 'Data/Test_december19.xls')



