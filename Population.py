#!/usr/bin/python
# -*- coding: utf-8 -*-

from Dorm import Dorm, Room
from random import randint
from Individual import Individual
from copy import deepcopy

from generate_people import generate_random_people


class Population:
    def __init__(self, number_of_individuals: int, number_of_students: int, ppl: list):
        """GENERATE INDIVIDUALS"""
        self.Individual_lst = list()
        self.number_of_students = number_of_students
        self.number_of_individuals = number_of_individuals
        self.Rooms = list()
        self.ppl = ppl
        for i in range(1, 6):
            for j in range(4):
                if j % 2 == 0:
                    self.Rooms.append(Room(number=i * 100 + j * 1, capacity=2, standard=randint(1, 3)))
                else:
                    self.Rooms.append(Room(number=i * 100 + j * 1, capacity=3, standard=randint(1, 3)))
        self.Dorm = Dorm("Test_dorm", self.Rooms, n_floors=5)
        for i in range(self.number_of_individuals):
            self.Individual_lst.append(Individual(self.number_of_students, deepcopy(self.Rooms), self.Dorm, deepcopy(self.ppl)))

        for individual in self.Individual_lst:
            individual.initialize_Individual()
            individual.set_rooms()

    def add_Individual(self, individual: Individual):
        self.Individual_lst.append(individual)

    def delete_Individual(self, individual: Individual):
        self.Individual_lst.remove(individual)

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
            # self.Individual_lst[i].initialize_Individual()
            score += f'     {self.Individual_lst[i].calc_score()}       |'
            # self.Individual_lst[i].reset_rooms()

        print(score)