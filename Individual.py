#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import shuffle
from Dorm import Dorm
import numpy as np
from random import randint


class Individual:
    def __init__(self, length: int, dorm: Dorm, ppl: list):
        self.ppl = ppl
        self.arr_bin = np.zeros((length, 1))
        self.dorm = dorm
        self.length = length
        self.score = None
        """To simulation"""
        self.calc_rank()

        self.room_register = {}
        self.rullet_percent = 0
        self.chose_list = np.array([0 for _ in range(length)])
        self.n_of_mutations = 0
        self.score_lst = list()
        self.mutation_lst = list()

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

    def actualize_Individual(self, flag_act=True, it=0, mutation_type: int = 0):
        self.reset_rooms()
        self.set_rooms()
        self.calc_score()
        if mutation_type != 0:
            self.mutation_lst.append([it, mutation_type])
        if flag_act:
            self.check_diversity()
            self.score_lst.append(self.score)

    def calc_score(self):
        """COST FUNCTION"""
        score = 0
        for student in self.ppl:
            ach = student.score # change
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
            if len(set(x)) != 1:
                total_punish += 150

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
                    total_punish += 25 #if there is a room with bigger n of people than capacity -> punish
            else:
                total_punish += 20 # if there is no even one person in room make bigger punish
        return total_punish

    def calc_rank(self):
        """This function calculate ranking of students and assign place in ranking for everyone"""
        ranking = dict()
        for person in self.ppl:
            ranking[person.PESEL] = person.calc_achievements()
        rank_sorted = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
        for place, (pesel, _) in enumerate(rank_sorted, 1):
            for person in self.ppl:
                if person.PESEL == pesel:
                    person.rank = place

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

    def check_diversity(self):
        """This function is responsible for checking whether every single Student were tried to fit and also how diverse
        algorithm works
        """
        for i in range(self.length):
            if self.arr_bin[i] != 0:
                self.chose_list[i] += 1

    def end_cleaning(self):
        """This function is responsible for kicking out people from multi-rooms and putting them to rooms with free spots"""
        students_to_replace = list()
        for room in self.dorm.all_rooms:
            if room.capacity < len(room.members):
                room.members.sort(key=lambda x: x.score, reverse=True)
                students_to_replace.extend(room.members[room.capacity:])
                for member in room.members[room.capacity:]:
                    member.actual_room = None
                    self.arr_bin[member.i] = 0

                room.members = room.members[:room.capacity]

        for room in self.dorm.all_rooms:
            sex = list(set([member.sex for member in room.members]))
            if len(sex) == 0:
                options = ['M', 'F']
                sex = list(options[randint(0, 1)])
            while room.capacity > len(room.members):
                popped_member = None
                if students_to_replace:
                    popped_member = students_to_replace.pop()
                else:
                    sorted_lst = sorted(self.ppl, key=lambda x: x.score, reverse=True)
                    for student in sorted_lst:
                        if student.actual_room is None and student.sex in sex and popped_member is None:
                            popped_member = student

                room.members.append(popped_member)
                popped_member.actual_room = room
                self.arr_bin[popped_member.i] = room.number
        self.actualize_Individual()

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
    pass

