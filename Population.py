#!/usr/bin/python
# -*- coding: utf-8 -*-

from Dorm import Dorm, Room
from random import randint
from Individual import Individual
from generate_people import generate_random_people


class Population:
    def __init__(self, number_of_individual: int, number_of_students: int, ppl: list):
        """GENERATE INDIVIDUALS"""
        self.Individual_lst = list()
        self.Rooms = list()
        self.ppl = ppl
        for i in range(1, 6):
            for j in range(4):
                if j % 2 == 0:
                    self.Rooms.append(Room(number=i * 100 + j * 1, capacity=2, standard=randint(1, 3)))
                else:
                    self.Rooms.append(Room(number=i * 100 + j * 1, capacity=3, standard=randint(1, 3)))
        self.Dorm = Dorm("Test_dorm", self.Rooms, n_floors=5)
        for i in range(number_of_individual):
            self.Individual_lst.append(Individual(number_of_students, self.Rooms, self.Dorm, self.ppl))

        for individual in self.Individual_lst:
            individual.initialize_Individual()
            individual.set_rooms()

    def add_Individual(self, individual: Individual):
        self.Individual_lst.append(individual)

    def delete_Individual(self, individual: Individual):
        self.Individual_lst.remove(individual)

    #TODO write function to present Population readibly
