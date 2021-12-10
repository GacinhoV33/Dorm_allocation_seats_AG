#!/usr/bin/python
# -*- coding: utf-8 -*

from matplotlib import pyplot as plt


def show_best_score(bst_score: list):
    """Function shows best score from population through time of iterations"""
    n_of_iteration = len(bst_score)
    iterations = [i for i in range(n_of_iteration)]
    plt.figure(num=1)
    plt.xlabel("N of iteration")
    plt.ylabel("Score")
    plt.grid()
    plt.scatter(iterations, bst_score)
    plt.show()


def show_score_individual(score_lst: list):
    """Function shows score of Individual through time of iterations. Color - RED"""
    n_of_iteration = len(score_lst)
    iterations = [i for i in range(n_of_iteration)]
    plt.figure(num=1)
    plt.xlabel("N of iteration")
    plt.ylabel("Score")
    plt.grid()
    plt.plot(iterations, score_lst, c='r')
    plt.show()


def show_frequency_Individual(frequency_lst: list):
    """Functions shows frequency of every student. #TODO"""
    n_of_iteration = len(frequency_lst)
    iterations = [i for i in range(n_of_iteration)]
    plt.figure(num=1)
    plt.xlabel("N of student")
    plt.ylabel("Frequency")
    plt.grid()
    plt.bar(iterations, frequency_lst)
    plt.show()