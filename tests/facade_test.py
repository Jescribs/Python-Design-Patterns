import unittest
from context import sample
from sample.facade import ElectricianUnion, MisDepartment, FacilitiesDepartment, FacilitiesFacade, States, StatesEU, StatesFD

class MisDepartmentTest(unittest.TestCase):
    def test_checkOnStatus(self):
        tech = MisDepartment()
        for _ in range(len(States)-2):
            self.assertEqual(tech.checkOnStatus(), 0)
        self.assertEqual(tech.checkOnStatus(), 1)

    def submitNetworkRequestTest(self):
        tech = MisDepartment()
        for _ in range(len(States)-2):
            self.assertEqual(tech.checkOnStatus(), 0)
        # Submit network request and restart state to zero
        tech.submitNetworkRequest()
        self.assertEqual(tech.checkOnStatus(), 0)

class ElectricianUnionTest(unittest.TestCase):
    def test_checkOnStatus(self):
        elect = ElectricianUnion()
        for _ in range(len(StatesEU)-2):
            self.assertEqual(elect.checkOnStatus(), 0)
        self.assertEqual(elect.checkOnStatus(), 1)

    def submitNetworkRequestTest(self):
        elect = ElectricianUnion()
        for _ in range(len(StatesEU)-2):
            self.assertEqual(elect.checkOnStatus(), 0)
        # Submit network request and restart state to zero
        elect.submitNetworkRequest()
        self.assertEqual(elect.checkOnStatus(), 0)

class FacilitiesDepartmentTest(unittest.TestCase):
    def test_checkOnStatus(self):
        eng = FacilitiesDepartment()
        for _ in range(len(StatesFD)-2):
            self.assertEqual(eng.checkOnStatus(), 0)
        self.assertEqual(eng.checkOnStatus(), 1)

    def submitNetworkRequestTest(self):
        eng = FacilitiesDepartment()
        for _ in range(len(StatesFD)-2):
            self.assertEqual(eng.checkOnStatus(), 0)
        # Submit network request and restart state to zero
        eng.submitNetworkRequest()
        self.assertEqual(eng.checkOnStatus(), 0)


class FacilitiesFacadeTest(unittest.TestCase):
    total_iterations= len(StatesFD) - 1 + len(StatesEU) - 1 + len(States) - 1

    def test_checkOnStatusFacade(self):
        facade = FacilitiesFacade()
        facade.submitNetworkRequest()
        total_iterations= len(StatesFD) - 1 + len(StatesEU) - 1 + len(States) - 1
        for _ in range(total_iterations):
            self.assertNotEqual(facade.checkOnStatus(), 1)
        self.assertEqual(facade.checkOnStatus(), 1)

    def submitNetworkRequestTest(self):
        facade = FacilitiesFacade()
        for _ in range(total_iterations):
            self.assertNotEqual(facade.checkOnStatus(), 1)
        # Submit network request and restart state to zero
        facade.submitNetworkRequest()
        self.assertNotEqual(facade.checkOnStatus(), 1)


if __name__ == '__main__':
    unittest.main()