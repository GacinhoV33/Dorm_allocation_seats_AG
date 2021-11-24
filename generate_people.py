#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import random


Male_first_names = ("Aaron", "Adam", "Adrian", "Adolf", "Albert", "Artur", "Alfred", "Aleksander", "Arkadiusz", 
                    "Bartłomiej", "Bartosz", "Beniamin", "Błażej", "Bogdan", "Bogusław", "Bryan", 
                    "Cezary", "Czesław", 
                    "Daniel", "Damian", "Dawid", "Darek", "Dominik", 
                    "Edward", "Ernest", "Eryk", "Eustachy",
                    "Filip", "Florian", "Felix", "Franciszek",
                    "Gabriel", "Gracjan", "Grzegorz", 
                    "Henryk", "Hubert",
                    "Ignacy", "Igor", "Ireneusz",
                    "Jacek", "Jakub", "Janusz", "Jarosław", "Jan", "Jędrzej", "Józef", "Julian", 
                    "Kacper", "Kajetan", "Klaudiusz", "Kamil", "Karol", "Kornel", "Konrad", "Krystian", "Krzysztof", "Kazimierz",
                    "Leonard", "Ludwik", 
                    "Łukasz", 
                    "Maciej", "Maksymilian", "Marcel", "Marek", "Marian", "Mateusz", "Mariusz", "Mikołaj", "Mirosław", "Max", "Marcin",
                    "Nikodem", "Norbert", 
                    "Oliwier", "Oskar", 
                    "Patryk", "Paweł", "Piotr", "Przemysław", 
                    "Radosław", "Rafał", "Ryszard", "Roman", "Robert", "Remigiusz",
                    "Samuel", "Sebastian", "Szymon", "Stanisław",
                    "Tadeusz", "Tytus", "Tomasz",
                    "Wacław", "Wiktor", "Witold", "Władysław", "Wojciech",
                    "Zdzisław", "Zbigniew", "Zygmunt"
                    )

Female_first_names = ("Ada", "Adrianna", "Agata", "Agnieszka", "Aleksandra", "Alicja", "Amanda", "Amelia", "Anastazja", "Aneta", "Angelika", "Aniela", "Anita", "Anna", "Asia", 
                    "Barbara", "Beata", "Bożena", "Bogusława", "Bianka", "Bernadetta",
                    "Celina", 
                    "Dagmara", "Daria", "Dominika", "Diana", "Dorota", "Danuta",
                    "Edyta", "Elżbieta", "Emilia", "Ewelina", "Ewa", "Eliza",
                    "Franciszka", "Faustyna",
                    "Gabriela", "Genowefa", "Greta", 
                    "Halina", "Hanna", "Helena", "Honorata",
                    "Ida", "Iga", "Ilona", "Irena", "Irmina", "Iwona", "Iza", "Izabela", 
                    "Jadwiga", "Jagoda", "Janina", "Jola", "Julia", "Justyna", "Jowita",
                    "Kaja", "Kamila", "Karina", "Karolina", "Kinga", "Katarzyna", "Kornelia", "Klaudia", 
                    "Lara", "Laura", "Luiza", 
                    "Łucja",
                    "Magda", "Magdalena", "Maja", "Marcelina", "Mariola", "Marysia", "Marlena", "Marta", "Marzena", "Matylda", "Michalina", "Milena", "Monika",
                    "Nadia", "Natalia", "Natasza", "Nikola", "Nina",
                    "Ola", "Oliwia", "Olga", 
                    "Patrycja", "Pamela", "Paulina", 
                    "Roksana", "Rozalia", "Renata", 
                    "Sandra", "Sara", "Sylwia", "Stefania", "Stanisława", 
                    "Teresa", 
                    "Vanessa", 
                    "Wanda", "Weronika", "Wiktoria", "Wioletta", "Władysława",
                    "Zofia", "Zuzanna"
                    )

Male_last_names = ("Nowak", "Kowalski", "Wiśniewski", "Wójcik", "Kowalczyk", "Kamiński", "Lewandowski", "Zieliński",
                    "Szymański", "Woźniak", "Kozłowski", "Jankowski", "Mazur", "Wojciechowski",
                    "Kwiatkowski", "Krawczyk", "Kaczmarek", "Piotrowski", "Grabowski", "Zając", "Pawłowski", "Michalski",
                    "Król", "Nowakowski", "Wieczorek", "Wróbel", "Jabłoński", "Dudek",
                    "Adamczyk", "Majewski", "Nowicki", "Olszewski", "Stępień", "Jaworski", "Malinowski", "Pawlak",
                    "Górski", "Witkowski", "Walczak", "Sikora", "Butkowski", "Baran", "Michalak", "Szewczyk", "Ostrowski",
                    "Tomaszewski", "Pietrzak", "Duda", "Zalewski", "Wróblewski"
                    )

Female_last_names = ("Nowak", "Kowalska", "Wiśniewska", "Wójcik", "Kowalczyk", "Kamińska", "Lewandowska", "Zielińska",
                     "Szymańska", "Dąbrowska", "Woźniak", "Kozłowska", "Jankowska", "Mazur", "Kwiatkowska", "Wojciechowska",
                     "Krawczyk", "Kaczmarek", "Piotrowska", "Grabowska", "Pawłowska", "Michalska", "Zając", "Król", "Wieczorek",
                     "Jabłońska", "Wróbel", "Nowakowska", "Majewska", "Olszewska", "Adamczyk", "Jaworska", "Malinowska",
                     "Stępień", "Dudek", "Górska", "Nowicka", "Pawlak", "Witkowska"

)

def generate_random_people(n:int = 100) ->list:
    """ CREATING DATA """
    male_first_names, female_first_names = generate_first_name(n//2, n//2)
    male_last_names, female_last_names = generate_last_name(n//2, n//2)


    """ CREATING INSTANCES OF CLASS STUDENT"""

def generate_first_name(males_number: int=0, females_number: int=0) ->tuple:
    amount = males_number + females_number 
    male_names = list()
    females_names = list()
    for i in range(males_number):
        male_names.append(Male_first_names[random.randint(0, len(Male_first_names)-1)])
    for _ in range(females_number):
        females_names.append(Female_first_names[random.randint(0, len(Female_first_names)-1)])
    if amount != len(male_names) + len(females_names):
        raise ValueError("Wrong generation of names!")
    return male_names, females_names


def generate_last_name(males_number: int, females_number: int) ->tuple:
    amount = males_number + females_number 
    male_names = list()
    females_names = list()
    for i in range(males_number):
        male_names.append(Male_first_names[random.randint(0, len(Male_last_names)-1)])
    for _ in range(females_number):
        females_names.append(Female_first_names[random.randint(0, len(Female_last_names)-1)])
    if amount != len(male_names) + len(females_names):
        raise ValueError("Wrong generation of names!")
    return male_names, females_names


def generate_distance(number_of_people: int, diversity: int=0) ->list:
    """ Diversity describes how randomly generated distances should be. Range 1-10
        #TODO implement diversity
    """
    distances = list()
    for _ in range(number_of_people):
        """#TODO check maximum range in Poland from Krakow to boards"""
        distances.append(random.randint(1, 1000))
    return distances


def generate_year_of_study(number_of_people: int) ->list:
    """#TODO Consult whether this function should create First Year student or not"""
    y_of_study = list()
    for _ in range(number_of_people):
        y_of_study.append(random.randint(1, 5))
    return y_of_study


def generate_standard(number_of_people: int) ->list:
    """#TODO Consult amount of standards (right now 3) """
    standards = list()
    for _ in range(number_of_people):
        standards.append(random.randint(1, 3))
    return standards


def generate_PESEL(number_of_people: int)->list:
    """"""
    def make_pesel():
        pesel = str
        for _ in range(6):
            pesel += str(random.randint(0, 9))
        return pesel

    PESELs = list()    
    for _ in range(number_of_people):
        p = make_pesel()
        while p not in PESELs:
            p = make_pesel()
        PESELs.append(p)
    return PESELs


def generate_income(number_of_people: int)->list:
    incomes = list()
    for _ in range(number_of_people):
        r = random.randint(1, 5):
        if r==1:
            incomes.append(random.randint(0, 1000))
        elif r==2:
            incomes.append(random.randint(1001, 2500))
        elif r==3:
            incomes.append(random.randint(2501, 5000))
        elif r==4:
            incomes.append(random.randint(5001, 10000))    
        elif r==5:
            incomes.append(random.randint(10001, 25000))
        else:
            raise ValueError("Error.")
    return incomes


def generate_friends_in_room(number_of_people: int) -> list:
    #TODO 
    pass 


generate_random_people(50)
