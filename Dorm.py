#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
from Student import Student
""" Capacity is always 2 or 3"""
#TODO CREATE MEANINGFUL DORM DATASET


class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.members = list()

    def add_locator(self, locator: Student):
        if len(self.members) >= self.capacity:
            return ValueError("Too many people in room")
        self.members.append(locator)

    def delete_locator(self, locator: Student):
        """Possible error while one person takes two slots in room"""
        self.members.remove(locator)


class Dorm:
    def __init__(self, name: str, rooms_standard_1: list, rooms_standard_2: list, rooms_standard_3: list):
        self.name = name
        self.rooms_standard_1 = rooms_standard_1
        self.rooms_standard_2 = rooms_standard_2
        self.rooms_standard_3 = rooms_standard_3
        self.all_rooms = rooms_standard_1 + rooms_standard_2 + rooms_standard_3



