#!/usr/bin/python
# -*- coding: utf-8 -*-

""" ZALOZENIA ODNOŚNIE PARAMETRÓW STUDENTA """
"""
year_of_studies -> przedział (1-5)

friends_in_room -> lista PESELI osób z którymi chce mieszkać 

PESEL -> PAMIĘTAC ŻE TO STRING 


"""


class Student:
    def __init__(self, first_name: str, last_name: str, distance: float, year_of_studies: int,
                 standard_of_room: int, income: float, gpa: float,  PESEL: str, sex: str, friends_in_room: list = None):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.distance = distance
        self.year_of_studies = year_of_studies
        self.standard_of_room = standard_of_room
        self.PESEL = PESEL
        self.income = income
        if self.year_of_studies == 1 and gpa is not None:
            raise ImportWarning("Invalid data imported. There's no gpa when year == 1")
        self.gpa = gpa
        self.friends_in_room = friends_in_room

    def __str__(self):
        return f'Name: {self.first_name} {self.last_name}\n ID: {self.PESEL}'