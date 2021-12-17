#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import shuffle
from Dorm import Dorm
import numpy as np
""""""


class Individual:
    def __init__(self, length: int, dorm: Dorm, ppl: list):
        self.ppl = ppl
        self.arr_bin = np.zeros((length, 1))
        # self.rooms = rooms
        self.dorm = dorm
        self.length = length
        self.score = None
        
        """To simulation"""
        self.room_register = {}
        self.rullet_percent = 0
        self.chose_list = np.array([0 for _ in range(length)])
        self.n_of_mutations = 0
        self.score_lst = list()

    def initialize_Individual(self):
        c = 0
        for room in self.dorm.all_rooms:
            for _ in range(room.capacity):
                self.arr_bin[c] = room.number
                c += 1
        np.random.shuffle(self.arr_bin)
        self.set_rooms()
        self.calc_score()
        self.score_lst.append(self.score)

    def actualize_rooms(self):
        # for student_n_room in self.arr_bin:
        #     if student_n_room != 0:
                # self.dorm.find_room_by_number()
        pass

    def actualize_Individual(self, flag_act=True):
        #TODO - Actualize state of rooms through simulation. After every single iteration rooms should be actualize to
        #TODO - effectively calc punishment
        self.reset_rooms()
        self.set_rooms()
        self.calc_score()
        if flag_act:
            self.check_diversity()
            self.score_lst.append(self.score)

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

        for room in self.dorm.all_rooms:
            locators = room.members
            x = list()
            for locator in locators:
                x.append(locator.sex)
            if set(x) != 1:
                total_punish += 5

        """PUNISH FOR TOO MANY PPL IN THE SAME ROOM"""
        self.room_register = {}
        for n_room in self.arr_bin:
            if int(n_room) != 0:
                if str(int(n_room)) in self.room_register.keys():
                    self.room_register[str(int(n_room))] += 1
                else:
                    self.room_register[str(int(n_room))] = 1
        for room_n in self.dorm.room_numbers:
            if str(room_n) in self.room_register.keys():
                if self.room_register[str(room_n)] > self.dorm.find_room_by_number(room_n).capacity:
                    total_punish += 5 #if there is a room with bigger n of people than capacity -> punish
            else:
                total_punish += 10 # if there is no even one person in room make bigger punish

        return total_punish

    def show_room_diversity(self):
        self.room_register = {}
        for n_room in self.arr_bin:
            if int(n_room) != 0:
                if str(int(n_room)) in self.room_register.keys():
                    self.room_register[str(int(n_room))] += 1
                else:
                    self.room_register[str(int(n_room))] = 1
        print("-"*30)
        for key, value in self.room_register.items():
            print(f"Room {key} : {value}. Capacity: {self.dorm.find_room_by_number(int(key)).capacity}")

    def set_rooms(self):
        """ FUNCTION IS RESPONSIBLE FOR ASSIGNING ROOMS TO STUDENTS AFTER INITIALIZING"""
        """ MAY BE USED ALSO AFTER CROSSING, MUTATING ETC."""
        for i in range(len(self.ppl)):
            if self.arr_bin[i] != 0:
                room = self.dorm.find_room_by_number(int(self.arr_bin[i]))
                self.ppl[i].actual_room = room
                room.add_locator(self.ppl[i])

    def reset_rooms(self):
        for i in range(len(self.ppl)):
            self.ppl[i].actual_room = None
        for room in self.dorm.all_rooms:
            room.members = []

    def check_correctness(self,):
        """ TEST 1 - Length of array (it may change after crossing)"""
        if self.arr_bin.shape[0] != self.length:
            raise ValueError("Wrong operation on Individual. Shape of array is not correct.")

        """ TEST 2 - Amount of place granted for specific room (it may be too big after crossing)"""
        for room in self.dorm.all_rooms:
            c = 0
            for i in self.arr_bin:
                if int(room.number) == int(i):
                    c += 1
            if room.capacity != c:
                raise ValueError("Too many rooms granted for students.")

        """ TEST 3 - GIRLS NOT IN ROOMS WITH BOYS """

    def check_diversity(self):
        #TODO
        """This function is responsible for checking whether every single Student were tried to fit and also how diverse
        algorithm works
        """
        for i in range(self.length):
            if self.arr_bin[i] != 0:
                self.chose_list[i] += 1

    def end_cleaning(self):
        """This function is responsible for kicking out people from multi-rooms and putting them to rooms with free spots"""
        #TODO take care about changing places in arr_bin and calc_score one more time
        students_to_replace = list()
        for room in self.dorm.all_rooms:
            if room.capacity < len(room.members):
                room.members.sort(key=lambda x: x.score, reverse=True)
                students_to_replace.extend(room.members[:room.capacity])
                room.members = room.members[room.capacity:]

        for room in self.dorm.all_rooms:
            while room.capacity > len(room.members) and students_to_replace:
                room.members.append(students_to_replace.pop())

    def __repr__(self):
        return self.arr_bin

    def __ge__(self, other):
        return self.score >= other.score

    def __str__(self):
        return str(self.arr_bin)

    def __iter__(self):
        for room_number in self.arr_bin:
            yield int(room_number)


if __name__ == "__main__":
    lst = np.array([1, 3, 8, 0, 0, 1, 0, 2])
    shuffle(lst)