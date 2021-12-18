#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import time

import xlrd
import xlwt
import xlsxwriter
from xlutils import copy

from Student import Student
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


def check_best_in_excel(best_score: float, path: str):
    Workbook = xlrd.open_workbook(path)
    sheet = Workbook.sheet_by_index(0)
    best_score_excel = sheet.cell_value(1, 14)
    if best_score > best_score_excel:
        Workbook = copy.copy(Workbook)
        Workbook.get_sheet(0).write(1, 14, best_score)
        Workbook.save(f'{path}')


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
    people = generate_friends_in_room(len(people), people, 0.25)
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
    #TODO It may generete situation where one person was chosen more than twice and some information are lost, cause max friends limit is 2
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
        person.friends_in_room = list()
        for j in range(2):
            if fr_lst[i][j] != -1:
                person.friends_in_room.append(people[fr_lst[i][j]])

    print(f'friends list: {fr_lst}')
    return people


def find_by_PESEL(people: list, PESEL: str):
    for person in people:
        if person.PESEL == PESEL:
            return person
    return None


def read_from_excel(path: str) -> list:
    Workbook = xlrd.open_workbook(path)
    sheet = Workbook.sheet_by_index(0)
    people = list()
    data = list()
    for i in range(12):
        data.append(sheet.col_values(colx=i, start_rowx=2))

    for i in range(len(data[0])):
        people.append(Student(str(data[0][i]), str(data[1][i]),
                              float(data[3][i]), int(data[4][i]), int(data[5][i]),
                              float(data[7][i]), float(data[8][i]), str(data[6][i]),
                              str(data[2][i]), list(), False, i
                              )
                      )
    Pesels = sheet.col_values(colx=10, start_rowx=2)
    for i, person in enumerate(people):
        if len(Pesels[i]) > 0:
            for pesel in Pesels[i]:
                person.friends_in_room.append(find_by_PESEL(people, str(pesel)))
    return people


def write_to_excel(name: str, data: list):
    #TODO formats
    # WorkBook = xlsxwriter.Workbook(f'Data/{name}.xls')
    WorkBook = xlwt.Workbook(encoding="utf-8")
    # sheet = WorkBook.add_worksheet()
    sheet = WorkBook.add_sheet("Python Sheet1")
    Letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    Names = ["First Name", "Last Name", "Sex", "Distance", "Year of Studies", "Room standard",
             "PESEL", "Income", "GPA", "Friends in room", "Actual room", "Special"]
    for i, letter in enumerate(Letters):
        sheet.write(0, i, Names[i])

    # for i, student in enumerate(data, 0):
    #     sheet.write(f'{Letters[0]}{i+2}', f'{str(student.first_name)}')
    #     sheet.write(f'{Letters[1]}{i+2}', str(student.last_name))
    #     sheet.write(f'{Letters[2]}{i+2}', str(student.sex))
    #     sheet.write(f'{Letters[3]}{i+2}', str(student.distance))
    #     sheet.write(f'{Letters[4]}{i+2}', str(student.year_of_studies))
    #     sheet.write(f'{Letters[5]}{i+2}', str(student.standard_of_room))
    #     sheet.write(f'{Letters[6]}{i+2}', str(student.PESEL))
    #     sheet.write(f'{Letters[7]}{i+2}', str(student.income))
    #     sheet.write(f'{Letters[8]}{i+2}', str(round(student.gpa, 4)))
    #     fr_str = " ".join([str(friend.PESEL) for friend in student.friends_in_room])
    #     sheet.write(f'{Letters[9]}{i+2}', str(fr_str))
    #     sheet.write(f'{Letters[10]}{i+2}', str(student.actual_room))
    #     sheet.write(f'{Letters[11]}{i+2}', str(student.is_special))

    for i, student in enumerate(data, 0):
        sheet.write(i+1, 0, f'{str(student.first_name)}')
        sheet.write(i+1, 1, str(student.last_name))
        sheet.write(i+1, 2, str(student.sex))
        sheet.write(i+1, 3, str(student.distance))
        sheet.write(i+1, 4, str(student.year_of_studies))
        sheet.write(i+1, 5, str(student.standard_of_room))
        sheet.write(i+1, 6, str(student.PESEL))
        sheet.write(i+1, 7, str(student.income))
        sheet.write(i+1, 8, str(round(student.gpa, 4)))
        fr_str = " ".join([str(friend.PESEL) for friend in student.friends_in_room])
        sheet.write(i+1, 9, str(fr_str))
        sheet.write(i+1, 10, str(student.actual_room))
        sheet.write(i+1, 11, str(student.is_special))

    WorkBook.save(f"Data/{name}.xls")
    print("-----WRITING TO EXCEL DONE-----")


if __name__ == "__main__":
    t = time.time()
    ppl = generate_random_people(100)
    """Writing data to excel"""
    write_to_excel("Main1", ppl)

    print(len(ppl))
    at = time.time()
    print(f"It took {float(at - t)} seconds.")
    check_best_in_excel(150, "Data/Test_december19.xls")