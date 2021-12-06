import unittest
from Dorm import Dorm
from generate_people import generate_random_people


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
        """THIS TEST HELPED WITH AVOIDING DUPLICATE THE EXACT SAME STUDENTS :) """
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


if __name__ == "__main__":
    unittest.main()

    