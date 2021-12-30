#!/usr/bin/python
# -*- coding: utf-8 -*-

from fpdf import FPDF
from datetime import date
import time
from generate_people import generate_random_people


class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.file_path = f'Reports/{date.today()} {time.strftime("%H%M")}.pdf'
        self.n_of_students = 200
        self.n_of_place = 100
        self.dorm_name = 'Filutek'
        self.n_of_3room = 20
        self.n_of_2room = 20
        self.ppl = generate_random_people(100)

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
        self.cell(w=200, h=10, align='C', txt='Simulation', ln=1)
        self.set_font('Arial', '', 14)
        self.cell(w=200, h=10, txt=f'Number of students: {self.n_of_students}', ln=1)
        self.cell(w=200, h=10, txt=f'Dorm name: {self.dorm_name}', ln=1)
        self.cell(w=200, h=10, txt=f'Number of place in dorm: {self.n_of_place}', ln=1)
        self.cell(w=200, h=10, txt=f'Rooms: {self.n_of_3room} x 3people  {self.n_of_2room} x 2people')

    def second_page(self):
        """People who gets room"""
        self.add_page()
        self.set_font('Arial', 'BI', 16)
        self.cell(w=200, h=10, ln=1, align='C', txt="Results")
        self.set_font('Arial', '', 14)
        help_flag = 0
        for i, person in enumerate(self.ppl):
            if i % 22 == 0:
                if help_flag == 1:
                    self.cell(200, h=10, ln=1)
                else:
                    help_flag += 1
                self.cell(200, h=10, ln=1)

            self.cell(w=200, h=10, txt=f'{person.first_name} {person.last_name}', ln=1)

        #TODO pętla for przechodząca po każdym i pokazująca czy się dostał

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

doc = PDF()
doc.generate()


# print(time.strftime("%H:%M"))
# pdf = FPDF()
#
# pdf.add_page()
# pdf.set_font("Arial", size=15)
# pdf.image('images/logoAGH.png', x=0, y=0, w=200, h=50, align='W')
#
# pdf.cell(200, 10, txt="Dorm seats allocation with using Genetic Algorithm", ln=1, align='C')
# pdf.output("TestReport.pdf")


