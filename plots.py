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


def show_score_individual(score_lst: list, mutation_lst: list):
    """Function shows score of Individual through time of iterations. Color - RED"""
    """Preparing Data to plot."""
    mutations = ['MUTATION_NON', 'MUTATION_SWAP']
    cmap_ = ['MUTATION_NON' if point[1] == 1 else 'MUTATION_SWAP' for point in mutation_lst]

    for i in range(len(mutation_lst)):
        mutation_lst[i][1] = score_lst[mutation_lst[i][0]]
    n_of_iteration = len(score_lst)
    iterations = [i for i in range(n_of_iteration)]
    plt.figure(num=1, figsize=[30, 15])
    for i, mut in enumerate(['MUTATION_NON', 'MUTATION_SWAP']):
        plt.plot([point[0] for j, point in enumerate(mutation_lst) if cmap_[j] == mutations[i]],
                 [point[1] for j, point in enumerate(mutation_lst) if cmap_[j] == mutations[i]],
                 marker='o', linestyle='', markersize=12, label=mut)
    plt.xlabel("N of iteration")
    plt.ylabel("Score")
    plt.grid()
    plt.title('Score of Individual through the iterations')
    plt.plot(iterations, score_lst, c='r', label='Score')
    plt.legend()
    plt.show()


def show_frequency_Individual(frequency_lst: list):
    """Functions shows frequency of every student. #TODO"""
    n_of_iteration = len(frequency_lst)
    iterations = [i for i in range(n_of_iteration)]
    plt.figure(num=1)
    plt.xlabel("N of student")
    plt.ylabel("Frequency")
    plt.grid()
    plt.scatter(iterations, frequency_lst, c='g')
    plt.show()