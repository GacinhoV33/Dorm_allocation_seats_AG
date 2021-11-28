#!/usr/bin/python
# -*- coding: utf-8 -*-
from Student import Student
from random import shuffle
from Dorm import Dorm, Room, Rooms
from generate_people import ppl
import numpy as np
""""""


class Individual:
    def __init__(self, length: int, rooms: list, dorm: Dorm, ppl: list):
        self.ppl = ppl
        self.arr_bin = np.zeros((length, 1))
        self.rooms = rooms
        self.dorm = dorm

    def initialize_Individual(self):
        c = 0
        for room in self.rooms:
            for _ in range(room.capacity):
                self.arr_bin[c] = room.number
                c += 1
        np.random.shuffle(self.arr_bin)
        self.set_rooms()

    def calc_score(self, students_lst: list):
        """FUNKCJA CELU"""
        score = 0
        for student in students_lst:
            ach = student.calc_achievements()
            sat = student.calc_satisfaction()
            score += (sat * ach)
        return score

    def set_rooms(self):
        for i in range(len(self.ppl)):
            if self.arr_bin[i] != 0:
                room = self.dorm.find_room_by_number(self.arr_bin[i])
                self.ppl[i].actual_room = room

    def __repr__(self):
        return self.arr_bin

    def __str__(self):
        return str(self.arr_bin.transpose())


if __name__ == "__main__":
    lst = np.array([1, 3, 8, 0, 0, 1, 0, 2])
    shuffle(lst)
    print(lst)

    # test_Individual = Individual(200, Rooms)
    # test_Individual.initialize_Individual()
    # print(test_Individual)
    # """ SOMETHING IS NO YES -> too many 100 rooms"""