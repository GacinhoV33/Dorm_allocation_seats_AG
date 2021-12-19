#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyautogui
import numpy as np
from random import randint, random
from Dorm import Dorm
from Individual import Individual
from copy import deepcopy

MUTATION_NON = 1
MUTATION_SWAP = 2


class Population:
    def __init__(self, number_of_individuals: int, number_of_students: int, ppl: list, dorm: Dorm,
                 number_of_iterations: int=20, mutation_non_included_probability: float=0.1,
                 mutation_swap_probability: float=0.1, info_flag: bool=True):
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
        self.init_Individuals()

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
            individual.set_rooms()
            if self.best_solution:
                if individual.score:
                    if individual.score > self.best_solution.score: #TODO change eq and compare objects
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
        individual1.actualize_Individual(), individual2.actualize_Individual()

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
        list(map(self.mutation_swap, self.Individual_lst, [it for _ in range(self.number_of_individuals)]))
        if it > 5:
            list(map(self.mutation_add_non_included, self.Individual_lst, [it for _ in range(self.number_of_individuals)]))

    def mutation_swap(self,  individual, it: int = 0):
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
        """ STEPS: FIND STUDENT WITH HIGHEST FREQUENCY
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

            individual.actualize_Individual(flag_act=False, it=actual_iteration, mutation_type=MUTATION_NON)

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

    def ShowProgress(self, current_iteration):
        """Uncomment to clear terminal after every iteration"""
        # pyautogui.click(x=996, y=907)
        # pyautogui.hotkey('command', 'l')
        percent = current_iteration/self.number_of_iterations
        print(f"Simulation in progress: \n[{int(percent*100)*'-'}{(100-int(percent*100))*' '}] {int(percent*100)}% \n")
        print(f'Iteration: {current_iteration}/{self.number_of_iterations}')

    def Genetic_Algorithm(self, ):
        for i in range(self.number_of_iterations):
            """MUTACJA"""
            self.mutate_population(i)
            """SELEKCJA"""
            self.rullet_selection()
            """KRZYŻOWANIE"""
            #TODO think about slot place
            self.cross_population()
            self.check_best()
            """To simulation"""
            if self.info_flag:
                self.best_solutions_lst.append(self.best_solution.score)
                self.ShowProgress(i)
                self.best_solutions_iter.append(self.find_best_in_iter())

        for individual in self.Individual_lst:
            # individual.show_room_diversity()
            individual.end_cleaning() # Function responsible for making solution acceptable
            individual.calc_score()

        self.check_best()
        print(self.Individual_lst[0].dorm)

        print(''*10, f"BEST SOLUTION GETS {self.best_solution.score} points!", ''*10)
        # self.print_freq()
        self.print_pop()

    def check_best(self):
        for individual in self.Individual_lst:
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
        score = f"Score|"
        for i in range(self.number_of_individuals):
            score += f'     {self.Individual_lst[i].score}      |'
        print(score, "\n\n")

