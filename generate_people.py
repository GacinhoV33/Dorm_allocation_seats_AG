#!/usr/bin/python
# -*- coding: utf-8 -*-

from Student import Student
import xlsxwriter
import random
import time


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
                    "Kacper", "Kajetan", "Klaudiusz", "Kamil", "Karol", "Kornel", "Konrad", "Krystian", "Krzysztof",
                    "Kazimierz",
                    "Leonard", "Ludwik",
                    "Łukasz",
                    "Maciej", "Maksymilian", "Marcel", "Marek", "Marian", "Mateusz", "Mariusz", "Mikołaj", "Mirosław",
                    "Max", "Marcin",
                    "Nikodem", "Norbert",
                    "Oliwier", "Oskar",
                    "Patryk", "Paweł", "Piotr", "Przemysław",
                    "Radosław", "Rafał", "Ryszard", "Roman", "Robert", "Remigiusz",
                    "Samuel", "Sebastian", "Szymon", "Stanisław",
                    "Tadeusz", "Tytus", "Tomasz",
                    "Wacław", "Wiktor", "Witold", "Władysław", "Wojciech",
                    "Zdzisław", "Zbigniew", "Zygmunt"
                    )

Female_first_names = (
    "Ada", "Adrianna", "Agata", "Agnieszka", "Aleksandra", "Alicja", "Amanda", "Amelia", "Anastazja", "Aneta",
    "Angelika",
    "Aniela", "Anita", "Anna", "Asia",
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
    "Magda", "Magdalena", "Maja", "Marcelina", "Mariola", "Marysia", "Marlena", "Marta", "Marzena", "Matylda",
    "Michalina",
    "Milena", "Monika",
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
                   "Górski", "Witkowski", "Walczak", "Sikora", "Butkowski", "Baran", "Michalak", "Szewczyk",
                   "Ostrowski",
                   "Tomaszewski", "Pietrzak", "Duda", "Zalewski", "Wróblewski"
                   )

Female_last_names = ("Nowak", "Kowalska", "Wiśniewska", "Wójcik", "Kowalczyk", "Kamińska", "Lewandowska", "Zielińska",
                     "Szymańska", "Dąbrowska", "Woźniak", "Kozłowska", "Jankowska", "Mazur", "Kwiatkowska",
                     "Wojciechowska",
                     "Krawczyk", "Kaczmarek", "Piotrowska", "Grabowska", "Pawłowska", "Michalska", "Zając", "Król",
                     "Wieczorek",
                     "Jabłońska", "Wróbel", "Nowakowska", "Majewska", "Olszewska", "Adamczyk", "Jaworska", "Malinowska",
                     "Stępień", "Dudek", "Górska", "Nowicka", "Pawlak", "Witkowska"

                     )


def generate_random_people(n:int = 100) -> list:
    """ CREATING DATA """
    male_first_names, female_first_names = generate_first_name(n//2, n//2)
    male_last_names, female_last_names = generate_last_name(n//2, n//2)
    distances = generate_distance(n)
    y_of_study = generate_year_of_study(n)
    standards = generate_standard(n)
    PESELs = generate_PESEL(n)
    incomes = generate_income(n)
    """First year students shouldn't have a GPA """
    gpas = generate_gpa(n)
    # write_to_excel("First_test", [(male_first_names+female_first_names), (male_last_names+female_last_names),
    #                 distances, y_of_study, standards, PESELs, incomes, gpas
    # ])

    """ CREATING INSTANCES OF CLASS STUDENT"""
    people = list()
    for i in range(int(n / 2)):
        people.append(Student(
            female_first_names[i], female_last_names[i],
            distances[i], y_of_study[i], standards[i], incomes[i], gpas[i], PESELs[i], sex='F')
        )
        people.append(Student(
            male_first_names[-i-1], male_last_names[-i-1],
            distances[-i-1], y_of_study[-i-1], standards[-i-1], incomes[-i-1], gpas[-i-1], PESELs[-i-1], sex='M')
        )
    """TEST WHETHER FUNCTION WORKS PROPERLY #TODO"""
    people = generate_friends_in_room(len(people), people, 0.09)
    return people


def generate_gpa(n: int) -> list:
    gpas = list()
    for _ in range(n):
        r = random.randint(2, 4)
        r += random.random()
        gpas.append(r)
    return gpas


def generate_first_name(males_number: int = 0, females_number: int = 0) -> tuple:
    amount = males_number + females_number
    male_names = list()
    females_names = list()
    for _ in range(males_number):
        male_names.append(Male_first_names[random.randint(0, len(Male_first_names) - 1)])
    for _ in range(females_number):
        females_names.append(Female_first_names[random.randint(0, len(Female_first_names) - 1)])
    if amount != len(male_names) + len(females_names):
        raise ValueError("Wrong generation of names!")
    return male_names, females_names


def generate_last_name(males_number: int, females_number: int) -> tuple:
    amount = males_number + females_number
    male_names = list()
    females_names = list()
    for i in range(males_number):
        male_names.append(Male_last_names[random.randint(0, len(Male_last_names) - 1)])
    for _ in range(females_number):
        females_names.append(Female_last_names[random.randint(0, len(Female_last_names) - 1)])
    if amount != len(male_names) + len(females_names):
        raise ValueError("Wrong generation of names!")
    return male_names, females_names


def generate_distance(number_of_people: int, diversity: int = 0) -> list:
    """ Diversity describes how randomly generated distances should be. Range 1-10
        #TODO implement diversity
    """
    distances = list()
    for _ in range(number_of_people):
        """#TODO check maximum range in Poland from Krakow to boards"""
        distances.append(random.randint(1, 1000))
    return distances


def generate_year_of_study(number_of_people: int) -> list:
    """#TODO Consult whether this function should create First Year student or not"""
    y_of_study = list()
    for _ in range(number_of_people):
        y_of_study.append(random.randint(1, 5))
    return y_of_study


def generate_standard(number_of_people: int) -> list:
    """#TODO Consult amount of standards (right now 3) """
    standards = list()
    for _ in range(number_of_people):
        standards.append(random.randint(1, 3))
    return standards


def generate_PESEL(number_of_people: int) -> list:
    PESELs = random.sample(range(1000, 10000), number_of_people)
    return PESELs


def generate_income(number_of_people: int) -> list:
    #TODO think about good criterium of score
    incomes = list()
    for _ in range(number_of_people):
        r = random.randint(1, 5)
        if r == 1:
            incomes.append(random.randint(0, 1000))
        elif r == 2:
            incomes.append(random.randint(1001, 2500))
        elif r == 3:
            incomes.append(random.randint(2501, 5000))
        elif r == 4:
            incomes.append(random.randint(5001, 10000))
        elif r == 5:
            incomes.append(random.randint(10001, 25000))
        else:
            raise ValueError("Error.")
    return incomes


def generate_friends_in_room(number_of_people: int, people: list, p: float) -> list:
    """parameter p is responsible for amount of people who wants friends in room"""
    fr_lst = [[-1, -1] for _ in range(number_of_people)]
    for j in range(number_of_people):
        for i in range(2):
            """CHECKING PROBABILITY"""
            r = random.random()
            if r <= p and fr_lst[j][i] == -1:
                f = random.randint(0, number_of_people-1)
                fr_lst[j][i] = f
                fr_lst[f][i] = j
    for i, person in enumerate(people):
        for j in range(2):
            if fr_lst[i][j] != -1:
                person.friends_in_room.append(people[i])

    print(f'friends list: {fr_lst}')
    return people


def write_to_excel(name: str, data: list):
    #TODO FILIP
    WorkBook = xlsxwriter.Workbook(f'Data/{name}.xlsx')
    sheet = WorkBook.add_worksheet()
    Letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    for i, student in enumerate(data):
        sheet.write_row(i, 1, f'{str(student.first_name)}')
        sheet.write_row(i, 2, str(student.last_name))
        sheet.write_row(i, 3, str(student.sex))
        sheet.write_row(i, 4, str(student.distance))
        sheet.write_row(i, 5, str(student.year_of_studies))
        sheet.write_row(i, 6, str(student.standard_of_room))
        sheet.write_row(i, 7, str(student.PESEL))
        sheet.write_row(i, 8, str(student.income))
        sheet.write_row(i, 9, str(student.gpa))
        sheet.write_row(i, 10, str(student.friends_in_room))
        sheet.write_row(i, 11, str(student.actual_room))
        sheet.write_row(i, 12, str(student.is_special))

    WorkBook.close()



t = time.time()
# ppl = generate_random_people(100)
"""Writing data to excel"""

at = time.time()
print(f"It took {float(at - t)} seconds.")
