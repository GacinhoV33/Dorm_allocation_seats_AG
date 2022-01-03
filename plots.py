#!/usr/bin/python
# -*- coding: utf-8 -*

from matplotlib import pyplot as plt

#TODO
# 1 Punishment through iterations (for specific individual)
# 2 Punishment through iterations with actual score (for specific individual)
# 3 Comparison the tournament selection with rullet
# 4 Comparison with and without mutations
# 5


def show_best_score(bst_score: list):
    """Function shows best score from population through time of iterations"""
    n_of_iteration = len(bst_score)
    iterations = [i for i in range(n_of_iteration)]
    plt.figure(num=1)
    plt.xlabel("N of iteration")
    plt.ylabel("Score")
    plt.title("Best solution")
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
    plt.figure(num=2, figsize=[30, 15])
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
    plt.figure(num=3)
    plt.xlabel("N of student")
    plt.ylabel("Frequency")
    plt.title("Frequency of students")
    plt.grid()
    plt.scatter(iterations, frequency_lst, c='g')
    plt.show()


def show_best_score_iter(best_solutions: list, n_of_individuals: int):
    """ This function shows how best solution in whole population change through iterations"""
    plt.figure(num=4, figsize=[20, 12])
    plt.plot([i for i in range(len(best_solutions))], best_solutions, c='r', label="Highest Score in population in iteration")
    plt.xlabel("Iterations")
    plt.ylabel("Best score in whole generation")
    plt.title("Best solution which exist in specific iteration")
    plt.grid()
    plt.title(f'{len(best_solutions)} Iterations. {n_of_individuals} Individuals.')
    plt.legend()
    plt.show()