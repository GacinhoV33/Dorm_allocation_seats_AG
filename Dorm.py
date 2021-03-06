#!/usr/bin/python
# -*- coding: utf-8 -*-

from Student import Student

"""
STANDARD - 1, 2, 3 where 3 is the best
ROOMS - 2 or 3 people
"""


class Room:
    def __init__(self, number: int, capacity: int, standard: int, floor: int):
        self.number = number
        self.capacity = capacity
        self.members = list()
        self.standard = standard
        self.floor = floor

    def add_locator(self, locator: Student):
        if isinstance(locator, Student):
            self.members.append(locator)

    def delete_locator(self, locator: Student):
        """Possible error while one person takes two slots in room"""
        if locator in self.members:
            self.members.remove(locator)


class Dorm:
    def __init__(self, name: str, n_floors: int, n_rooms: int, ppl: list):
        self.name = name
        self.rooms_standard_1 = list()
        self.rooms_standard_2 = list()
        self.rooms_standard_3 = list()
        self.all_rooms = list()
        self.n_rooms = n_rooms
        self.n_floors = n_floors
        self.ppl = ppl
        self.create_rooms()
        self.room_numbers = set([room.number for room in self.all_rooms])
        self.number_of_places = self.count_nr_of_places()

    def count_nr_of_places(self):
        capacity = 0
        for room in self.all_rooms:
            capacity += room.capacity
        return capacity

    def find_room_by_number(self, number: int) -> Room:
        """Function find instance of class Room assigned to its number."""
        for room in self.all_rooms:
            if room.number == number:
                return room

    def divide_rooms_via_standard(self, ):
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

    def create_rooms(self):
        """This function is responsible for creating rooms."""
        for i in range(1, self.n_floors + 1):
            for j in range(self.n_rooms):
                if j % 2 == 0:
                    if j % 3 == 0:
                        self.all_rooms.append(Room(number=i * 100 + j * 1, capacity=2, standard=1, floor=i))
                    elif j % 3 == 1:
                        self.all_rooms.append(Room(number=i * 100 + j * 1, capacity=2, standard=2, floor=i))
                    elif j % 3 == 2:
                        self.all_rooms.append(Room(number=i * 100 + j * 1, capacity=2, standard=3, floor=i))
                else:
                    if j % 3 == 0:
                        self.all_rooms.append(Room(number=i * 100 + j * 1, capacity=3, standard=1, floor=i))
                    elif j % 3 == 1:
                        self.all_rooms.append(Room(number=i * 100 + j * 1, capacity=3, standard=2, floor=i))
                    elif j % 3 == 2:
                        self.all_rooms.append(Room(number=i * 100 + j * 1, capacity=3, standard=3, floor=i))

    def __str__(self, ):
        return str(f" Dorm Name:{self.name} \n " + " ".join(
            [f'Floor Number: 'f'{room.floor}\n '
             f'     Door number: {room.number}\n '
             f'     Standard: {room.standard}\n '
             f'     Capacity: {room.capacity}\n'
             f'     Locators: {[memb for memb in room.members]}\n '
             f'     ----------------\n' if str(room.number)[1:] == "00"
             else
             f'     Door number: {room.number}\n '
             f'     Standard: {room.standard}\n '
             f'     Capacity: {room.capacity}\n'
             f'     Locators: {[memb for memb in room.members]}\n '
             '      ----------------\n'
             for room in self.all_rooms]))