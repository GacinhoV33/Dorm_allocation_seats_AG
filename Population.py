#!/usr/bin/python
# -*- coding: utf-8 -*-
from Student import Student
from random import shuffle
from Dorm import Dorm, Room, Rooms
import numpy as np
""""""


class Population:
    def __init__(self, length: int, rooms: list):
        self.arr_bin = np.zeros((length, 1))
        self.rooms = rooms

    def initialize_population(self):
        c = 0
        for i, room in enumerate(self.rooms, 0):
            for _ in range(room.capacity):
                self.arr_bin[i+c] = room.number
                c += 1
        shuffle(self.arr_bin)

    def __repr__(self):
        return self.arr_bin

    def __str__(self):
        return str(self.arr_bin.transpose())


if __name__ == "__main__":
    test_population = Population(200, Rooms)
    test_population.initialize_population()
    print(test_population)
    """ SOMETHING IS NO YES -> too many 100 rooms"""