#!/usr/bin/python
# -*- coding: utf-8 -*-

from Dorm import Dorm
from Individual import Individual
from copy import deepcopy


class Population:
    def __init__(self, number_of_individuals: int, number_of_students: int, ppl: list, dorm: Dorm):
        """GENERATE INDIVIDUALS"""
        self.Individual_lst = list()
        self.number_of_students = number_of_students
        self.number_of_individuals = number_of_individuals
        """ppl is list of instances of Student class"""
        self.ppl = ppl
        self.dorm = dorm

        """INITIALIZING STRUCTURES"""
        self.Rooms = self.dorm.all_rooms
        self.init_Individuals()

    def init_Individuals(self):
        for i in range(self.number_of_individuals):
            self.Individual_lst.append(
                Individual(self.number_of_students, deepcopy(self.Rooms), self.dorm, deepcopy(self.ppl))
            )
        for individual in self.Individual_lst:
            individual.initialize_Individual()
            individual.set_rooms()

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
            score += f'     {self.Individual_lst[i].calc_score()}      |'
        print(score)