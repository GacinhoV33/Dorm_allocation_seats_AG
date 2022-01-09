import unittest
from Dorm import Dorm
from generate_people import generate_random_people
from Population import Population


class TestDorm(unittest.TestCase):
    def test_room_amount(self):
        dorm = Dorm("TEST_DORM", 5, 100, generate_random_people())
        Rooms = dorm.all_rooms
        self.assertAlmostEqual(dorm.n_floors, 5)
        self.assertEqual(len(dorm.all_rooms), len(Rooms))

    def test_floors(self, ):
        dorm = Dorm("TEST_DORM",  5, 100, generate_random_people())
        highest_floor = 0
        for room in dorm.all_rooms:
            if room.number // 100 > highest_floor:
                highest_floor = room.number // 100

        self.assertEqual(dorm.n_floors, highest_floor)


class TestGenerate(unittest.TestCase):

    def test_IDs(self, ):
        ppl = generate_random_people(50)
        retval = True
        PESELS = list()
        for person in ppl:
            PESELS.append(person.PESEL)

        if len(set(PESELS)) != len(PESELS):
            retval = False
            print(len(set(PESELS)))
            print(len(PESELS))
        self.assertEqual(retval, True)


class TestPopulation(unittest.TestCase):
    dorm = Dorm("TEST_DORM",   n_floors=5, n_rooms=4,  ppl=generate_random_people())
    pop = Population(20, len(dorm.ppl), dorm.ppl, dorm, 30)

    def test_Pop_params(self):
        dorm = Dorm("TEST_DORM", n_floors=5, n_rooms=4, ppl=generate_random_people())
        pop = Population(20, len(dorm.ppl), dorm.ppl, dorm, 30)
        self.assertEqual(pop.number_of_individuals, 20)
        self.assertEqual(len(pop.Individual_lst), 20)
        self.assertNotEqual(pop.best_solution, None)
        self.assertEqual(len(pop.best_solutions_lst), 0)

    def test_Pop(self):
        dorm = Dorm("TEST_DORM", n_floors=5, n_rooms=4, ppl=generate_random_people())
        pop = Population(20, len(dorm.ppl), dorm.ppl, dorm, 30)
        pop.Genetic_Algorithm()
        self.assertEqual(pop.number_of_individuals, 20)
        self.assertNotEqual(pop.best_solution, None)
        self.assertEqual(len(pop.Individual_lst[3].score_lst), 30)


if __name__ == "__main__":
    unittest.main()


    