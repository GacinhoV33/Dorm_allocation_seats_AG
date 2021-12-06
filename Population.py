#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint, random
from Dorm import Dorm
from Individual import Individual
from copy import deepcopy


class Population:
    def __init__(self, number_of_individuals: int, number_of_students: int, ppl: list, dorm: Dorm, number_of_iterations: int=20):
        """GENERATE INDIVIDUALS"""
        self.Individual_lst = list()
        self.number_of_students = number_of_students
        self.number_of_individuals = number_of_individuals
        """ppl is list of instances of Student class"""
        self.ppl = ppl
        self.dorm = dorm

        """INITIALIZING STRUCTURES"""
        self.Rooms = self.dorm.all_rooms

        self.number_of_iterations = number_of_iterations
        self.best_solution = None
        self.init_Individuals()

    def init_Individuals(self):
        for i in range(self.number_of_individuals):
            self.Individual_lst.append(
                Individual(self.number_of_students, deepcopy(self.Rooms), self.dorm, deepcopy(self.ppl))
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

    def cross_population(self):
        pass

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

        r = [random() for _ in range(10)]
        for j in range(10):
            for i, individiual in enumerate(self.Individual_lst):
                    if rullet[i] < r[j] < rullet[i+1]:
                        generated_ind.append(individiual)
        for i in generated_ind:
            print(i.score)
        print(rullet)
         # TODO SOME ERROR WITH PRINTING




    def check_best(self):
        pass

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
        print(score)