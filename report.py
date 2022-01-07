#!/usr/bin/python
# -*- coding: utf-8 -*-

from fpdf import FPDF
from datetime import date
import time


class PDF(FPDF):
    def __init__(self, best_solution, iterations, individuals, rullet_flag, rank_flag, tour_flag,  mut_add_flag,
                 mut_swap_flag, mut_add_prob, mut_swap_prob, computing_time):
        super().__init__()
        self.file_path = f'Reports/{date.today()}{time.strftime("%H%M")}.pdf'
        self.n_of_students = 200
        self.n_of_place = 100
        self.dorm_name = 'Filutek'
        self.n_of_3room = 20
        self.n_of_2room = 20
        self.ppl = best_solution.ppl
        self.iterations = iterations
        self.individuals = individuals
        self.rullet_flag = rullet_flag
        self.rank_flag = rank_flag
        self.tour_flag = tour_flag
        self.mut_add_flag = mut_add_flag
        self.mut_swap_flag = mut_swap_flag
        self.mut_add_prob = mut_add_prob
        self.mut_swap_prob = mut_swap_prob
        self.computing_time = computing_time

    def header(self):
        # Logo
        self.image('images/logoAGH.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(60)
        # Title
        self.cell(80, 10, 'Dorm Allocation Report', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def first_page(self):
        """Date, Time, Informations """
        self.add_page()
        self.cell(200, h=10, ln=1)
        self.cell(200, h=10, ln=1)
        self.cell(w=200, h=10, txt=f"Date: {date.today()}\n", ln=1)
        self.cell(w=200, h=10, txt=f"Time: {time.strftime('%H:%M:%S')}", ln=1)

        """Simulation"""
        self.cell(200, h=10, ln=1)
        self.set_font('Arial', 'B', 20)
        self.cell(w=200, h=10, align='C', txt='Data', ln=1)
        self.set_font('Arial', 'B', 14)
        self.cell(w=50, h=10, txt=f'Number of students:')
        self.set_font('Arial', '', 14)
        self.cell(w=60, h=10, txt=f'{self.n_of_students}', ln=1)

        self.set_font('Arial', 'B', 14)
        self.cell(w=60, h=10, txt=f'Number of place in dorm:')
        self.set_font('Arial', '', 14)
        self.cell(w=60, h=10, txt=f'{self.n_of_place}', ln=1)

        self.set_font('Arial', 'B', 14)
        self.cell(w=30, h=10, txt=f'Dorm name:')
        self.set_font('Arial', '', 14)
        self.cell(w=60, h=10, txt=f'{self.dorm_name}', ln=1)


        self.set_font('Arial', 'B', 20)
        self.cell(w=200, h=10, align='C', txt='Simulation Parameters', ln=1)
        self.set_font('Arial', 'B', 14)
        self.cell(w=24, h=10, txt=f'Iterations:')
        self.set_font('Arial', '', 14)
        self.cell(w=60, h=10, txt=f'{self.iterations}', ln=1)
        self.set_font('Arial', 'B', 14)
        self.cell(w=28, h=10, txt=f'Individuals:')
        self.set_font('Arial', '', 14)
        self.cell(w=60, h=10, txt=f'{self.individuals}', ln=1)
        self.set_font('Arial', 'B', 14)
        self.cell(w=24, h=10, txt=f'Selection:')
        if self.rank_flag:
            self.set_font('Arial', '', 14)
            self.cell(w=60, h=10, txt=f'Ranking Selection', ln=1)
        elif self.tour_flag:
            self.set_font('Arial', '', 14)
            self.cell(w=60, h=10, txt=f'Tournament Selection', ln=1)
        elif self.rullet_flag:
            self.set_font('Arial', '', 14)
            self.cell(w=60, h=10, txt=f'Roulette Selection', ln=1)
        else:
            self.cell(ln=1)

        self.set_font('Arial', 'B', 14)
        self.cell(w=40, h=10, txt='Mutations:', ln=1)
        if self.mut_add_flag:
            self.set_font('Arial', '', 14)
            self.cell(w=80, h=10, txt=f' - Add Non Included Mutation with probability {float(self.mut_add_prob * 100)}%', ln=1)
        if self.mut_swap_flag:
            self.set_font('Arial', '', 14)
            self.cell(w=80, h=10, txt=f' - Swap Mutation with probability {float(self.mut_add_prob) * 100}%', ln=1)
        if not self.mut_swap_flag and not self.mut_swap_flag:
            self.set_font('Arial', '', 14)
            self.cell(w=80, h=10, txt=' -None')

        self.set_font('Arial', 'B', 14)
        self.cell(w=40, h=10, txt=f'Computing Time: ')
        self.set_font('Arial', '', 14)
        self.cell(w=60, h=10, txt=f'{int(self.computing_time)} seconds.')

    def second_page(self):
        """People who gets room"""
        self.add_page()
        self.set_font('Arial', 'BI', 16)
        self.cell(w=200, h=10, ln=1, align='C', txt="Results")

        help_flag = 0
        for i, person in enumerate(self.ppl):
            """TABLE """
            if i % 22== 0:
                if help_flag == 1:
                    self.cell(200, h=10, ln=1)
                else:
                    help_flag += 1
                self.set_font('Arial', 'B', 12)
                self.cell(30, 10, "First name:")
                self.cell(30, 10, "Last name:")
                self.cell(30, 10, "Status:", align='C')
                self.cell(30, 10, "Standard:", align='C')
                self.cell(40, 10, "Friends in Room:", align='C')
                self.cell(30, 10, "Ranking:", align='C', ln=1)
                self.set_font('Arial', '', 12)
                self.set_text_color(10, 10, 10)

            # self.cell(200, h=10, ln=1)
            self.set_font('Arial', '', 12)
            self.set_text_color(10, 10, 10)
            self.cell(30, 10, f'{person.first_name}')
            self.cell(30, 10, f'{person.last_name}')
            self.set_font('Arial', 'I', 12)
            # self.cell(30, 10, 'Status: ')
            if person.actual_room is None:
                self.set_text_color(255, 0, 0)
                self.cell(30, 10, txt=f"Negative", align='C')
                self.cell(30, 10, txt='-', align='C')
                self.cell(40, 10, txt='-', align='C')

            else:
                self.set_text_color(0, 255, 0)
                self.cell(30, 10, txt=f"Room: {person.actual_room.number}", align='C')
                if not int(person.actual_room.standard) == int(person.standard_of_room):
                    self.set_text_color(10, 80, 10)
                self.cell(30, 10, txt=f'{person.actual_room.standard}', align='C')

                if person.friends_in_room:
                    for friend in person.friends_in_room:
                        if friend.actual_room:
                            if friend.actual_room.number == person.actual_room.number:
                                self.set_text_color(0, 255, 0)
                                self.cell(40//len(person.friends_in_room), 10, txt='V', align='C')
                            else:
                                self.set_text_color(255, 255, 255)
                                self.cell(40 // len(person.friends_in_room), 10, txt='O', align='C')
                        else:
                            self.set_text_color(255, 0, 0)
                            self.cell(40//len(person.friends_in_room), 10, txt='X', align='C')
                    # self.cell(40, 10, txt='TEST', align='C')
                    # for friend in person.friends_in_room:
                    #     if friend is None or friend is "None":
                    #         print("Sth wrong")
                    #         self.set_text_color(10, 80, 10)
                    #         # TODO solve wrong type in data
                    #     else:
                    #         self.cell(40/len(person.friends_in_room), 10, txt='F')
                else:
                    self.set_text_color(0, 255, 0)
                    self.cell(40, 10, txt='-', align='C')
            self.set_text_color(10, 10, 10)
            self.cell(30, 10, txt=str(person.rank), ln=1, align='C')

    def save(self):
        self.output(self.file_path)

    def generate(self):
        self.first_page()
        self.second_page()
        self.save()


def generate_report():
    doc = FPDF()
    doc.add_page()
    doc.output(f'Reports/{date.today()} {time.strftime("%H:%M")}')



