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
                 rullet_selection_flag: bool=True, tournament_selection_flag=False, rank_selection_flag:bool=False, info_flag:bool=True):
    if path:
        path_excel = "Data/Test_december19.xls"
        ppl = read_from_excel(path_excel)
    elif n_of_people:
        ppl = generate_random_people(n_of_people)
    else:
        raise ImportError("Running simulation without parameters")
    Simulation_Dorm = Dorm("Test_dorm", n_floors=5, n_rooms=6,  ppl=ppl)
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


if __name__ == "__main__":
    """ETAP 0 - stworzenie niezbędnych struktur i danych"""
    ppl = generate_random_people(500)
    path_excel = "Data/Test_december19.xls"
    # ppl = read_from_excel(path_excel)
    """ETAP 1 - Stworzenie Akademika"""
    Dorm_TEST = Dorm("Test_dorm", n_floors=5, n_rooms=6,  ppl=ppl)
    """ ETAP 2 - Stworzenie pierwszej populacji """
    test_population = Population(50, 500, ppl, Dorm_TEST, 150)

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
    show_best_score_iter(test_population.best_solutions_iter, test_population.number_of_individuals)
    check_best_in_excel(test_population.best_solution.score, 'Data/Test_december19.xls')



