#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

import xlrd
import xlwt

from Student import Student
Male_first_names = ("Aaron", "Adam", "Adrian", "Adolf", "Albert", "Artur", "Alfred", "Aleksander", "Arkadiusz",
                    "Bartlomiej", "Bartosz", "Beniamin", "Blazej", "Bogdan", "Boguslaw", "Bryan",
                    "Cezary", "Czeslaw",
                    "Daniel", "Damian", "Dawid", "Darek", "Dominik",
                    "Edward", "Ernest", "Eryk", "Eustachy",
                    "Filip", "Florian", "Felix", "Franciszek",
                    "Gabriel", "Gracjan", "Grzegorz",
                    "Henryk", "Hubert",
                    "Ignacy", "Igor", "Ireneusz",
                    "Jacek", "Jakub", "Janusz", "Jaroslaw", "Jan", "Jedrzej", "Jozef", "Julian",
                    "Kacper", "Kajetan", "Klaudiusz", "Kamil", "Karol", "Kornel", "Konrad", "Krystian", "Krzysztof",
                    "Kazimierz",
                    "Leonard", "Ludwik",
                    "Lukasz",
                    "Maciej", "Maksymilian", "Marcel", "Marek", "Marian", "Mateusz", "Mariusz", "Mikolaj", "Miroslaw",
                    "Max", "Marcin",
                    "Nikodem", "Norbert",
                    "Oliwier", "Oskar",
                    "Patryk", "Pawel", "Piotr", "Przemyslaw",
                    "Radoslaw", "Rafal", "Ryszard", "Roman", "Robert", "Remigiusz",
                    "Samuel", "Sebastian", "Szymon", "Stanislaw",
                    "Tadeusz", "Tytus", "Tomasz",
                    "Waclaw", "Wiktor", "Witold", "Wladyslaw", "Wojciech",
                    "Zdzislaw", "Zbigniew", "Zygmunt"
                    )

Female_first_names = (
    "Ada", "Adrianna", "Agata", "Agnieszka", "Aleksandra", "Alicja", "Amanda", "Amelia", "Anastazja", "Aneta",
    "Angelika",
    "Aniela", "Anita", "Anna", "Asia",
    "Barbara", "Beata", "Bozena", "Boguslawa", "Bianka", "Bernadetta",
    "Celina",
    "Dagmara", "Daria", "Dominika", "Diana", "Dorota", "Danuta",
    "Edyta", "Elzbieta", "Emilia", "Ewelina", "Ewa", "Eliza",
    "Franciszka", "Faustyna",
    "Gabriela", "Genowefa", "Greta",
    "Halina", "Hanna", "Helena", "Honorata",
    "Ida", "Iga", "Ilona", "Irena", "Irmina", "Iwona", "Iza", "Izabela",
    "Jadwiga", "Jagoda", "Janina", "Jola", "Julia", "Justyna", "Jowita",
    "Kaja", "Kamila", "Karina", "Karolina", "Kinga", "Katarzyna", "Kornelia", "Klaudia",
    "Lara", "Laura", "Luiza",
    "Lucja",
    "Magda", "Magdalena", "Maja", "Marcelina", "Mariola", "Marysia", "Marlena", "Marta", "Marzena", "Matylda",
    "Michalina",
    "Milena", "Monika",
    "Nadia", "Natalia", "Natasza", "Nikola", "Nina",
    "Ola", "Oliwia", "Olga",
    "Patrycja", "Pamela", "Paulina",
    "Roksana", "Rozalia", "Renata",
    "Sandra", "Sara", "Sylwia", "Stefania", "Stanislawa",
    "Teresa",
    "Vanessa",
    "Wanda", "Weronika", "Wiktoria", "Wioletta", "Wladyslawa",
    "Zofia", "Zuzanna"
)

Male_last_names = ("Nowak", "Kowalski", "Wisniewski", "Wojcik", "Kowalczyk", "Kaminski", "Lewandowski", "Zielinski",
                   "Szymanski", "Wozniak", "Kozlowski", "Jankowski", "Mazur", "Wojciechowski",
                   "Kwiatkowski", "Krawczyk", "Kaczmarek", "Piotrowski", "Grabowski", "Zajac", "Pawlowski", "Michalski",
                   "Krol", "Nowakowski", "Wieczorek", "Wrobel", "Jablonski", "Dudek",
                   "Adamczyk", "Majewski", "Nowicki", "Olszewski", "Stepien", "Jaworski", "Malinowski", "Pawlak",
                   "Gorski", "Witkowski", "Walczak", "Sikora", "Butkowski", "Baran", "Michalak", "Szewczyk",
                   "Ostrowski",
                   "Tomaszewski", "Pietrzak", "Duda", "Zalewski", "Wroblewski"
                   )

Female_last_names = ("Nowak", "Kowalska", "Wisniewska", "Wojcik", "Kowalczyk", "Kaminska", "Lewandowska", "Zielinska",
                     "Szymanska", "Dabrowska", "Wozniak", "Kozlowska", "Jankowska", "Mazur", "Kwiatkowska",
                     "Wojciechowska",
                     "Krawczyk", "Kaczmarek", "Piotrowska", "Grabowska", "Pawlowska", "Michalska", "Zajac", "Krol",
                     "Wieczorek",
                     "Jablonska", "Wrobel", "Nowakowska", "Majewska", "Olszewska", "Adamczyk", "Jaworska", "Malinowska",
                     "Stepien", "Dudek", "Gorska", "Nowicka", "Pawlak", "Witkowska"
                     )
# 
# Male_first_names = ("Aaron", "Adam", "Adrian", "Adolf", "Albert", "Artur", "Alfred", "Aleksander", "Arkadiusz",
#                     "Bartłomiej", "Bartosz", "Beniamin", "Błażej", "Bogdan", "Bogusław", "Bryan",
#                     "Cezary", "Czesław",
#                     "Daniel", "Damian", "Dawid", "Darek", "Dominik",
#                     "Edward", "Ernest", "Eryk", "Eustachy",
#                     "Filip", "Florian", "Felix", "Franciszek",
#                     "Gabriel", "Gracjan", "Grzegorz",
#                     "Henryk", "Hubert",
#                     "Ignacy", "Igor", "Ireneusz",
#                     "Jacek", "Jakub", "Janusz", "Jarosław", "Jan", "Jędrzej", "Józef", "Julian",
#                     "Kacper", "Kajetan", "Klaudiusz", "Kamil", "Karol", "Kornel", "Konrad", "Krystian", "Krzysztof",
#                     "Kazimierz",
#                     "Leonard", "Ludwik",
#                     "Łukasz",
#                     "Maciej", "Maksymilian", "Marcel", "Marek", "Marian", "Mateusz", "Mariusz", "Mikołaj", "Mirosław",
#                     "Max", "Marcin",
#                     "Nikodem", "Norbert",
#                     "Oliwier", "Oskar",
#                     "Patryk", "Paweł", "Piotr", "Przemysław",
#                     "Radosław", "Rafał", "Ryszard", "Roman", "Robert", "Remigiusz",
#                     "Samuel", "Sebastian", "Szymon", "Stanisław",
#                     "Tadeusz", "Tytus", "Tomasz",
#                     "Wacław", "Wiktor", "Witold", "Władysław", "Wojciech",
#                     "Zdzisław", "Zbigniew", "Zygmunt"
#                     )
# 
# Female_first_names = (
#     "Ada", "Adrianna", "Agata", "Agnieszka", "Aleksandra", "Alicja", "Amanda", "Amelia", "Anastazja", "Aneta",
#     "Angelika",
#     "Aniela", "Anita", "Anna", "Asia",
#     "Barbara", "Beata", "Bożena", "Bogusława", "Bianka", "Bernadetta",
#     "Celina",
#     "Dagmara", "Daria", "Dominika", "Diana", "Dorota", "Danuta",
#     "Edyta", "Elżbieta", "Emilia", "Ewelina", "Ewa", "Eliza",
#     "Franciszka", "Faustyna",
#     "Gabriela", "Genowefa", "Greta",
#     "Halina", "Hanna", "Helena", "Honorata",
#     "Ida", "Iga", "Ilona", "Irena", "Irmina", "Iwona", "Iza", "Izabela",
#     "Jadwiga", "Jagoda", "Janina", "Jola", "Julia", "Justyna", "Jowita",
#     "Kaja", "Kamila", "Karina", "Karolina", "Kinga", "Katarzyna", "Kornelia", "Klaudia",
#     "Lara", "Laura", "Luiza",
#     "Łucja",
#     "Magda", "Magdalena", "Maja", "Marcelina", "Mariola", "Marysia", "Marlena", "Marta", "Marzena", "Matylda",
#     "Michalina",
#     "Milena", "Monika",
#     "Nadia", "Natalia", "Natasza", "Nikola", "Nina",
#     "Ola", "Oliwia", "Olga",
#     "Patrycja", "Pamela", "Paulina",
#     "Roksana", "Rozalia", "Renata",
#     "Sandra", "Sara", "Sylwia", "Stefania", "Stanisława",
#     "Teresa",
#     "Vanessa",
#     "Wanda", "Weronika", "Wiktoria", "Wioletta", "Władysława",
#     "Zofia", "Zuzanna"
# )
# 
# Male_last_names = ("Nowak", "Kowalski", "Wiśniewski", "Wójcik", "Kowalczyk", "Kamiński", "Lewandowski", "Zieliński",
#                    "Szymański", "Woźniak", "Kozłowski", "Jankowski", "Mazur", "Wojciechowski",
#                    "Kwiatkowski", "Krawczyk", "Kaczmarek", "Piotrowski", "Grabowski", "Zając", "Pawłowski", "Michalski",
#                    "Król", "Nowakowski", "Wieczorek", "Wróbel", "Jabłoński", "Dudek",
#                    "Adamczyk", "Majewski", "Nowicki", "Olszewski", "Stępień", "Jaworski", "Malinowski", "Pawlak",
#                    "Górski", "Witkowski", "Walczak", "Sikora", "Butkowski", "Baran", "Michalak", "Szewczyk",
#                    "Ostrowski",
#                    "Tomaszewski", "Pietrzak", "Duda", "Zalewski", "Wróblewski"
#                    )
# 
# Female_last_names = ("Nowak", "Kowalska", "Wiśniewska", "Wójcik", "Kowalczyk", "Kamińska", "Lewandowska", "Zielińska",
#                      "Szymańska", "Dąbrowska", "Woźniak", "Kozłowska", "Jankowska", "Mazur", "Kwiatkowska",
#                      "Wojciechowska",
#                      "Krawczyk", "Kaczmarek", "Piotrowska", "Grabowska", "Pawłowska", "Michalska", "Zając", "Król",
#                      "Wieczorek",
#                      "Jabłońska", "Wróbel", "Nowakowska", "Majewska", "Olszewska", "Adamczyk", "Jaworska", "Malinowska",
#                      "Stępień", "Dudek", "Górska", "Nowicka", "Pawlak", "Witkowska"
#                      )


def generate_random_people(n:int = 100) -> list:
    """ CREATING DATA """
    male_first_names, female_first_names = generate_first_name(n//2, n//2)
    male_last_names, female_last_names = generate_last_name(n//2, n//2)
    distances = generate_distance(n)
    y_of_study = generate_year_of_study(n)
    standards = generate_standard(n)
    PESELs = generate_PESEL(n)
    incomes = generate_income(n)
    gpas = generate_gpa(n)
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
    """TEST WHETHER FUNCTION WORKS PROPERLY"""
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


def generate_distance(number_of_people: int) -> list:
    distances = list()
    for _ in range(number_of_people):
        distances.append(random.randint(1, 1000))
    return distances


def generate_year_of_study(number_of_people: int) -> list:
    y_of_study = list()
    for _ in range(number_of_people):
        y_of_study.append(random.randint(1, 5))
    return y_of_study


def generate_standard(number_of_people: int) -> list:
    standards = list()
    for _ in range(number_of_people):
        standards.append(random.randint(1, 3))
    return standards


def generate_PESEL(number_of_people: int) -> list:
    PESELs = random.sample(range(1000, 10000), number_of_people)
    return PESELs


def generate_income(number_of_people: int) -> list:
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
                Sex_flag = True
                while Sex_flag:
                    f = random.randint(0, number_of_people-1)
                    if people[f].sex == people[j].sex and f != j:
                        Sex_flag = False
                fr_lst[j][i] = f
                fr_lst[f][i] = j
    for i, person in enumerate(people):
        person.friends_in_room = list()
        for j in range(2):
            if fr_lst[i][j] != -1 and fr_lst[i][j] is not None:
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
        data.append(sheet.col_values(colx=i, start_rowx=1))

    for i in range(len(data[0])):

        people.append(Student(str(data[0][i]), str(data[1][i]),
                              float(data[3][i]), int(data[4][i]), int(data[5][i]),
                              float(data[7][i]), float(data[8][i]), str(data[6][i]),
                              str(data[2][i]), list(), False, None, i
                              )
                      )
    Pesels = sheet.col_values(colx=9, start_rowx=1)
    for i, person in enumerate(people):
        if len(Pesels[i]) > 0:
            for pesel in Pesels[i].split():
                founded_person = find_by_PESEL(people, str(pesel))
                if founded_person:
                    person.friends_in_room.append(founded_person)
    return people


def write_to_excel(name: str, data: list):
    WorkBook = xlwt.Workbook(encoding="utf-8")
    sheet = WorkBook.add_sheet("Python Sheet1")
    Letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    Names = ["First Name", "Last Name", "Sex", "Distance", "Year of Studies", "Room standard",
             "PESEL", "Income", "GPA", "Friends in room", "Actual room", "Special"]
    for i, letter in enumerate(Letters):
        sheet.write(0, i, Names[i])

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
        fr_str_list = list()
        for friend in student.friends_in_room:
            if friend is not None and friend.PESEL != "None":
                fr_str_list.append(str(friend.PESEL))
        fr_str = " ".join(fr_str_list)
        sheet.write(i+1, 9, str(fr_str))
        if student.actual_room:
            sheet.write(i+1, 10, str(student.actual_room.number))
        else:
            sheet.write(i+1, 10, str(student.actual_room))
        sheet.write(i+1, 11, str(student.is_special))

    WorkBook.save(name)
    print("-----WRITING TO EXCEL DONE-----")


if __name__ == "__main__":
    pass
