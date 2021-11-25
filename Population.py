#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import shuffle
import numpy as np
""""""


class Population:
    def __init__(self, length: int, rooms: list):
        self.arr_bin = np.zeros((1, length))
        self.rooms = rooms

    def initialize_population(self):
        for i, room in enumerate(self.rooms):
            self.arr_bin[i] = room.number
        shuffle(self.arr_bin)

    def __repr__(self):
        return self.arr_bin

    def __str__(self):
        return str(self.arr_bin)