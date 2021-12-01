import unittest
from Dorm import Dorm, Room, Rooms
from Population import Population
from generate_people import generate_random_people

class TestDorm(unittest.TestCase):
    
    def test_room_amount(self):
        # popul = Population(20, 100, generate_random_people(100))
        dorm = Dorm("TEST_DORM", Rooms, 5, generate_random_people())
        self.assertAlmostEqual(dorm.n_floors, 5)        
        self.assertEqual(len(dorm.all_rooms), len(Rooms))

    def test_floors(self,):
        dorm = Dorm("TEST_DORM", Rooms, 5, generate_random_people())
        highest_floor = 0
        for room in dorm.all_rooms:
            if room.number // 100 > highest_floor:
                highest_floor = room.number // 100
         
        self.assertEqual(dorm.n_floors, highest_floor)

    def test_IDs(self,):
        ppl = generate_random_people(75)
        retval = True
        PESELS = list()
        for person in ppl:
            PESELS.append(person.PESEL)

        if len(set(PESELS)) != len(PESELS):
            retval = False 
            print(len(set(PESELS)))
        self.assertEqual(retval, True)


if __name__ == "__main__":
    unittest.main()

    