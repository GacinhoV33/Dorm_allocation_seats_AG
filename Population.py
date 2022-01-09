#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from random import randint, random, shuffle
from Dorm import Dorm
from Individual import Individual
from copy import deepcopy
from tqdm import tqdm
from generate_people import write_to_excel
from datetime import date
import time
MUTATION_NON = 1
MUTATION_SWAP = 2


class Population:
    def __init__(self, number_of_individuals: int, number_of_students: int, ppl: list, dorm: Dorm,
                 number_of_iterations: int=20, mutation_non_included_probability: float=0.1,
                 mutation_swap_probability: float=0.1,
                 mutation_swap_flag: bool=True, mutation_non_included_flag:bool=True,
                 rullet_selection_flag: bool=True, tournament_selection_flag=False, rank_selection_flag:bool=False,
                 info_flag: bool=True):
        """GENERATE INDIVIDUALS"""
        self.Individual_lst = list()
        self.number_of_students = number_of_students
        self.number_of_individuals = number_of_individuals
        """ppl is list of instances of Student class"""
        self.ppl = ppl
        self.dorm = dorm

        """INITIALIZING STRUCTURES"""

        """To simulation"""
        self.info_flag = info_flag
        self.number_of_iterations = number_of_iterations
        self.best_solution = None
        self.best_solutions_lst = list()
        self.best_solutions_iter = list()
        self.mutaion_non_included_probability = mutation_non_included_probability
        self.mutation_swap_probability = mutation_swap_probability

        self.mutation_swap_flag = mutation_swap_flag
        self.mutation_non_included_flag = mutation_non_included_flag
        self.rullet_selection_flag = rullet_selection_flag
        self.tournament_selection_flag = tournament_selection_flag
        self.rank_selection_flag = rank_selection_flag
        self.init_Individuals()
        self.last_solution = None
        """ After Simulation"""

    def find_best_in_iter(self):
        scores = [individual.score for individual in self.Individual_lst]
        return max(scores)

    def init_Individuals(self):
        for i in range(self.number_of_individuals):
            self.Individual_lst.append(
                Individual(self.number_of_students, deepcopy(self.dorm), deepcopy(self.ppl))
            )
        for individual in self.Individual_lst:
            individual.initialize_Individual()
            if self.best_solution:
                if individual.score:
                    if individual.score > self.best_solution.score:
                        self.best_solution = individual
                else:
                    if individual.calc_score() > self.best_solution.score:
                        self.best_solution = individual
            else:
                self.best_solution = individual

    def add_Individual(self, individual: Individual):
        if isinstance(individual, Individual):
            self.Individual_lst.append(individual)

    def delete_Individual(self, individual: Individual):
        if isinstance(individual, Individual):
            if individual in self.Individual_lst:
                self.Individual_lst.remove(individual)
            else:
                print("Deleting none existing individual")
        else:
            raise ValueError("Wrong data type")

    def crossing(self, individual1: Individual, individual2: Individual):
        r = randint(0, self.number_of_students - 1)
        individual1.arr_bin[r:], individual2.arr_bin[r:] = individual2.arr_bin[r:], individual1.arr_bin[r:]
        individual1.actualize_Individual(flag_act=True)
        individual2.actualize_Individual(flag_act=True)

    def cross_population(self):
        """ We generate random int to chose in what way we should take individuals to crossing"""
        if randint(0, 2) % 2 == 0:
            """ 1 OPTION"""
            for i in range(self.number_of_individuals//2):
                self.crossing(self.Individual_lst[2*i], self.Individual_lst[2*i+1])
        else:
            """ 2 OPTION"""
            for i in range(self.number_of_individuals//2):
                self.crossing(self.Individual_lst[i], self.Individual_lst[-i-1])

    def mutate_population(self, it: int):
        if self.mutation_swap_flag:
            list(map(self.mutation_swap, self.Individual_lst, [it for _ in range(self.number_of_individuals)]))
        if it > self.number_of_iterations//4 and self.mutation_non_included_flag:
            list(map(self.mutation_add_non_included, self.Individual_lst, [it for _ in range(self.number_of_individuals)]))

    def mutation_swap(self,  individual, it: int = 0):
        """Mutation randomly chose student and replace him with another """
        r = randint(1, (self.number_of_students - 1)//2)
        if random() < self.mutation_swap_probability:
            beginning = individual.arr_bin[:r]
            end = individual.arr_bin[-r:]
            individual.arr_bin[:r] = end
            individual.arr_bin[-r:] = beginning
            individual.actualize_Individual(False, it, mutation_type=MUTATION_SWAP)
            individual.n_of_mutations += 1

    def mutation_add_non_included(self, individual, actual_iteration):
        """Mutation takes student with the highest frequence and replace it with the student with low frequence"""
        """ 
            STEPS: FIND STUDENT WITH HIGHEST FREQUENCY
                   FIND STUDENT WITH LOWEST FREQUENCY
                   REPLACE THEM  
        """
        if random() <= self.mutaion_non_included_probability:
            freq_low_lst = np.where(individual.chose_list == np.min(individual.chose_list))
            freq_max_lst = np.where(individual.chose_list == np.max(individual.chose_list))
            for i in range(min(len(freq_max_lst), len(freq_low_lst))):
                if individual.arr_bin[freq_max_lst[0][i]] != 0 and individual.arr_bin[freq_low_lst[0][i]] == 0:
                    individual.arr_bin[freq_low_lst[0][i]] = individual.arr_bin[freq_max_lst[0][i]]
                    individual.arr_bin[freq_max_lst[0][i]] = 0

            individual.actualize_Individual(False, it=actual_iteration, mutation_type=MUTATION_NON)
            individual.n_of_mutations += 1


    def rullet_selection(self):
        all_score = 0
        for individiual in self.Individual_lst:
            all_score += individiual.score

        generated_ind = list()
        rullet = [0]
        y = 0
        for i, individiual in enumerate(self.Individual_lst, 0):
            individiual.rullet_percent = individiual.score/all_score
            rullet.append(individiual.rullet_percent+y)
            y += individiual.rullet_percent

        r = [random() for _ in range(self.number_of_individuals)]
        for j in range(self.number_of_individuals):
            for i, individiual in enumerate(self.Individual_lst):
                    if rullet[i] < r[j] < rullet[i+1]:
                        generated_ind.append(deepcopy(individiual))

        self.Individual_lst = generated_ind

    def tournament_selection(self, ):
        """Tournament selection -> Every Individual 'fights' with his opponents. The one with bigger score stays and
        replicate, the other lose and is dropped out"""

        """Generating tow different sets of individuals and shuffle them"""

        r = randint(0, self.number_of_individuals // 2)

        first_group = [i for i in range(r, r+self.number_of_individuals//2)]
        second_group = [i for i in range(0, r)] + [j for j in range(r+self.number_of_individuals//2, self.number_of_individuals)]
        shuffle(first_group)
        shuffle(second_group)
        new_individuals = list()
        for first, second in zip(first_group, second_group):
            if self.Individual_lst[first].score > self.Individual_lst[second].score:
                """Replicate first and kick out second"""
                for _ in range(2):
                    new_individuals.append(deepcopy(self.Individual_lst[first]))

            elif self.Individual_lst[first].score < self.Individual_lst[second].score:
                """Replicate second and kick out first"""
                for _ in range(2):
                    new_individuals.append(deepcopy(self.Individual_lst[second]))

            else:
                """Nothing happen"""
                new_individuals.append(deepcopy(self.Individual_lst[first]))
                new_individuals.append(deepcopy(self.Individual_lst[second]))

        if self.number_of_individuals % 2 != 0: # added to prevent error when dividing into two groups
            new_individuals.append(self.Individual_lst[randint(0, self.number_of_individuals-1)])

        self.Individual_lst = new_individuals

    def rank_selection(self):
        all_scr = 0
        for ind in self.Individual_lst:
            all_scr += ind.score

        lst_of_copies = list()
        for ind in self.Individual_lst:
            for i in range(int((ind.score/all_scr * self.number_of_individuals))):
                lst_of_copies.append(deepcopy(ind))

        if len(lst_of_copies) < self.number_of_individuals:
            for _ in range(self.number_of_individuals-len(lst_of_copies)):
                lst_of_copies.append(deepcopy(self.Individual_lst[randint(0, self.number_of_individuals-1)]))

        self.Individual_lst = lst_of_copies

    def ShowProgress(self, current_iteration, label=None):
        """Uncomment to clear terminal after every iteration"""
        percent = current_iteration/self.number_of_iterations
        print(f"Simulation in progress: \n[{int(percent*100)*'-'}{(100-int(percent*100))*' '}] {int(percent*100)}% \n")
        print(f'Iteration: {current_iteration}/{self.number_of_iterations}')
        if label:
            pass


    def Genetic_Algorithm(self, ):
        for i in tqdm(range(self.number_of_iterations), desc='Simulation in progress: '):

            """SELEKCJA"""
            if self.tournament_selection_flag:
                self.tournament_selection()
            elif self.rullet_selection_flag:
                self.rullet_selection()
            elif self.rank_selection_flag:
                self.rank_selection()
            """KRZYŻOWANIE"""
            self.cross_population()
            """MUTACJA"""
            self.mutate_population(i)
            self.check_best()
            """To simulation"""
            if self.info_flag:
                self.best_solutions_lst.append(self.best_solution.score)
                self.best_solutions_iter.append(self.find_best_in_iter())

        for individual in self.Individual_lst:
            individual.end_cleaning() # Function responsible for making solution acceptable
            individual.calc_score()

        self.check_best()
        self.best_solution.end_cleaning()
        print(self.best_solution.dorm)
        if self.info_flag:
            self.best_solutions_lst.append(self.best_solution.score)
            self.best_solutions_iter.append(self.find_best_in_iter())
        print(''*10, f"BEST SOLUTION GETS {self.best_solution.score} points!", ''*10)

        self.write_best_solution()

        # self.print_pop()

    def write_best_solution(self):
        name = f'Solutions/{date.today()} {time.strftime("%H%M")}.xls'
        write_to_excel(name, self.best_solution.ppl)

    def check_best(self):
        for individual in self.Individual_lst:
            individual.end_cleaning()
            if individual.score > self.best_solution.score:
                self.best_solution = individual

    def print_freq(self):
        print("-"*20, "FREQUENCY", "-"*20)
        for j, individual in enumerate(self.Individual_lst):
            freq = 0
            for i in individual.chose_list:
                if i == 0:
                    freq += 1
            print(f"Individual number {j}: {freq} students weren't include in solution which is {freq/individual.length * 100}%. ")
            print(f"Rooms totally: {len(individual.dorm.all_rooms)} - Rooms included: {len(individual.room_register.keys())}")
            print("-" * 50)

    def print_pop(self, ):
        first_line = "       "  # 7 x space
        for n in range(self.number_of_individuals):
            first_line += f'Individual: {n} | '
        print(first_line)
        for i in range(len(self.ppl)):
            if i > 9:
                one_line = f"slot{i}|"
            else:
                one_line = f"slot{i} |"
            for j in range(self.number_of_individuals):
                if j == 0:
                    if int(self.Individual_lst[j].arr_bin[i]) > 0:
                        one_line += f'     {int(self.Individual_lst[j].arr_bin[i])}      |'
                    else:
                        one_line += f'     {int(self.Individual_lst[j].arr_bin[i])}        |'
                else:

                    if int(self.Individual_lst[j].arr_bin[i]) > 0:
                        one_line += f'     {int(self.Individual_lst[j].arr_bin[i])}       |'
                    else:
                        one_line += f'     {int(self.Individual_lst[j].arr_bin[i])}         |'

            print(one_line)
        score = f"Score| "
        for i in range(self.number_of_individuals):
            score += f'     {self.Individual_lst[i].score}      |'
        print(score, "\n\n")


