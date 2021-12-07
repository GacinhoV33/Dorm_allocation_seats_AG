#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import shuffle
from Dorm import Dorm
import numpy as np
""""""


class Individual:
    def __init__(self, length: int, rooms: list, dorm: Dorm, ppl: list):
        self.ppl = ppl
        self.arr_bin = np.zeros((length, 1))
        self.rooms = rooms
        self.dorm = dorm
        self.length = length
        self.score = None

        """To simulation"""
        self.rullet_percent = 0

    def initialize_Individual(self):
        c = 0
        for room in self.rooms:
            for _ in range(room.capacity):
                self.arr_bin[c] = room.number
                c += 1
        np.random.shuffle(self.arr_bin)
        self.set_rooms()
        self.calc_score()

    def actualize_Individual(self):
        self.reset_rooms()
        self.set_rooms()
        self.calc_score()

    def calc_score(self):
        """COST FUNCTION"""
        score = 0
        for student in self.ppl:
            ach = student.calc_achievements()
            sat = student.calc_satisfaction()
            score += (sat * ach)

        punish = self.calc_punishment()
        self.score = score - punish
        return self.score

    def calc_punishment(self):

        total_punish = 0
        """ PUNISH GIRLS AND BOYS IN THE SAME ROOM"""

        for room in self.rooms:
            locators = room.members
            x = list()
            for locator in locators:
                x.append(locator.sex)
            if set(x) != 1:
                total_punish += 5

        return total_punish

    def set_rooms(self):
        """ FUNCTION IS RESPONSIBLE FOR ASSIGNING ROOMS TO STUDENTS AFTER INITIALIZING"""
        """ MAY BE USED ALSO AFTER CROSSING, MUTATING ETC."""
        for i in range(len(self.ppl)):
            if self.arr_bin[i] != 0:
                room = self.dorm.find_room_by_number(self.arr_bin[i])
                self.ppl[i].actual_room = room
                room.add_locator(self.ppl[i])

    def reset_rooms(self):
        """ #TODO"""
        for i in range(len(self.ppl)):
            self.ppl[i].actual_room = None

    def check_correctness(self,):
        """ TEST 1 - Length of array (it may change after crossing)"""
        if self.arr_bin.shape[0] != self.length:
            raise ValueError("Wrong operation on Individual. Shape of array is not correct.")

        """ TEST 2 - Amount of place granted for specific room (it may be too big after crossing)"""
        for room in self.rooms:
            c = 0
            for i in self.arr_bin:
                if int(room.number) == int(i):
                    c += 1
            if room.capacity != c:
                raise ValueError("Too many rooms granted for students.")

        """ TEST 3 - GIRLS NOT IN ROOMS WITH BOYS """

    def __repr__(self):
        return self.arr_bin

    def __str__(self):
        return str(self.arr_bin)

    def __iter__(self):
        for room_number in self.arr_bin:
            yield int(room_number)


if __name__ == "__main__":
    lst = np.array([1, 3, 8, 0, 0, 1, 0, 2])
    shuffle(lst)