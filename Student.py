#!/usr/bin/python
# -*- coding: utf-8 -*-


class Student:
    def __init__(self, first_name: str, last_name: str, distance: float, year_of_studies: int,
                 standard_of_room: int, income: float, gpa: float,  PESEL: str, sex: str,
                 friends_in_room: list = list(), is_special=False, actual_room=None, i:int=0):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex

        self.distance = distance
        self.year_of_studies = year_of_studies
        self.standard_of_room = standard_of_room
        self.PESEL = PESEL
        self.income = income

        self.gpa = gpa
        self.friends_in_room = friends_in_room
        """ Gen"""
        self.is_special = is_special
        self.actual_room = actual_room

        self.i = i
        self.score = self.calc_achievements()
        self.rank = None

    def calc_achievements(self):
        score = 0
        if 4.5 < self.gpa <= 5:
            score += 10
        elif 4 < self.gpa <= 4.5:
            score += 6
        elif 3.5 < self.gpa <= 4:
            score += 4
        elif 3 < self.gpa <= 3.5:
            score += 1
        elif 0 <= self.gpa <= 3:
            score += 0
        else:
            raise ValueError("Wrong GPA value. It must be from 0 to 5.")

        if self.income > 4000:
            score += 1
        elif 3500 <= self.income < 4000:
            score += 4
        elif 3000 <= self.income < 3500:
            score += 6
        elif 2500 <= self.income < 3000:
            score += 7
        elif 0 <= self.income < 2500:
            score += 10
        else:
            raise ValueError("Wrong Income Value. Should be not less than 0.")

        if 50 <= self.distance <= 100:
            score += 1
        elif 100 < self.distance <= 200:
            score += 4
        elif 200 < self.distance <= 300:
            score += 8
        elif 300 < self.distance <= 400:
            score += 10
        elif self.distance > 400:
            score += 12
        return score

    def calc_satisfaction(self):
        """ JE??LI ZNAJOMI W POKOJU DODAJ PUNKTY"""
        """ JE??LI OTRZYMANO WYBRANY STANDARD DODAJ PUNKTY"""
        score = 0
        if self.actual_room:
            if self.friends_in_room:
                for friend in self.friends_in_room:
                    if friend:
                        if friend.actual_room:
                            if friend.actual_room.number == self.actual_room.number:
                                score += 30
            if self.standard_of_room == self.actual_room.standard:
                score += 10
        return score

    def set_room(self, room):
        self.actual_room = room

    def reset_room(self):
        self.actual_room = None

    def __str__(self):
        return f' Name: {self.first_name}\n Lastname: {self.last_name}\n ID: {self.PESEL}'

    def __repr__(self):
        return f" name: '{self.first_name}' lastname: '{self.last_name}' ID: '{self.PESEL}'"


if __name__ == "__main__":
    pass
