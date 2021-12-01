#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
from Student import Student
""" Capacity is always 2 or 3"""
#TODO CREATE MEANINGFUL DORM DATASET

"""
DORM - 5 floors : from 1 to 5
TOTAL NUMBER OF ROOMS - 100
STANDARD - 1, 2, 3 where 3 is the best
ROOMS - 2 or 3 people

1 floor -> 2 x 3 people  &  2 x 2 people      Number: from 1 to 4 (101 ... 104)
...
5 floor -> 2 x 3 people  &  2 x 2 people      Number: from 1 to 4 (501 ... 504)
"""


class Room:
    def __init__(self, number: int, capacity: int, standard: int):
        self.number = number
        self.capacity = capacity
        self.members = list()
        self.standard = standard

    def add_locator(self, locator: Student):
        if len(self.members) >= self.capacity:
            return ValueError("Too many people in room")
        self.members.append(locator)

    def delete_locator(self, locator: Student):
        """Possible error while one person takes two slots in room"""
        self.members.remove(locator)


class Dorm:
    def __init__(self, name: str, all_rooms: list, n_floors: int, ppl: list):
        self.name = name
        self.rooms_standard_1 = list()
        self.rooms_standard_2 = list()
        self.rooms_standard_3 = list()
        self.all_rooms = all_rooms
        self.n_floors = n_floors
        self.ppl = ppl

    def find_room_by_number(self, number: int) -> Room:
        """Function find instance of class Room by assigned to him number."""
        for room in self.all_rooms:
            if room.number == number:
                return room

    def divide_rooms_via_standard(self,):
        """This function divide rooms which were created with specific standard to 3 groups"""
        for room in self.all_rooms:
            if room.standard == 1:
                self.rooms_standard_1.append(room)
            elif room.standard == 2:
                self.rooms_standard_2.append(room)
            elif room.standard == 3:
                self.rooms_standard_3.append(room)
            else:
                raise ValueError("Wrong standard of room! ")

    def __str__(self,):
        #TODO DIVIDE IT BY FLOOR 
        return str(f"Dorm Name:{self.name} \n" + " ".join([f'Door number: {room.number}\n Locators: {[memb for memb in room.members]}\n Standard: {room.standard}\n-----------------\n' for room in self.all_rooms]))


Rooms = list()
for i in range(1, 6):
    for j in range(4):
        if j % 2 == 0:
            Rooms.append(Room(number=i * 100 + j * 1, capacity=2, standard=randint(1, 3)))
        else:
            Rooms.append(Room(number=i * 100 + j * 1, capacity=3, standard=randint(1, 3)))


