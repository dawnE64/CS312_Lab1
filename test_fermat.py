from unittest import TestCase

from fermat import fermat, mod_exp, fprobability


# Runs the fermat algorithm with numbers picked to try to trick it.
# k is the number of tests to run, and it is the second input.
class TestFermatAccuracy(TestCase):

    # Test primality of 1 through 10 since those are easy
    def test_fermat_first_ten(self):
        self.assertEqual('composite', fermat(1, 10))
        self.assertEqual('prime', fermat(2, 10))
        self.assertEqual('prime', fermat(3, 10))
        self.assertEqual('composite', fermat(4, 10))
        self.assertEqual('prime', fermat(5, 10))
        self.assertEqual('composite', fermat(6, 10))
        self.assertEqual('prime', fermat(7, 10))
        self.assertEqual('composite', fermat(8, 10))
        self.assertEqual('composite', fermat(9, 10))
        self.assertEqual('composite', fermat(10, 10))

    # Test some large numbers
    def test_fermat_large(self):
        self.assertEqual('prime', fermat(7853, 30))
        self.assertEqual('composite', fermat(7850, 30))

    # Test for gigantic prime
    def test_fermat_gigantic(self):
        self.assertEqual('prime', fermat(3130231163, 30))
        self.assertEqual('composite', fermat(3130231162, 30))

    # This test shows that the function is insufficient because it can't pick out a Carmichael number
    # In this test, k = 2
    def test_fermat_first_carmichael_1(self):
        for i in range(20):
            self.assertNotEqual('prime', fermat(561, 2))

    # This test has a k = 10
    def test_fermat_first_carmichael_2(self):
        for i in range(20):
            self.assertNotEqual('prime', fermat(561, 10))


# Pre-calculated probabilities compared to the function's computed output
class TestFermatProbability(TestCase):

    def test_fprobability_1(self):
        k = 10
        self.assertAlmostEqual(0.999023437500000, fprobability(k), places=15)
        print(f'expected vs got\n{0.999023437500000:.15f}\n{fprobability(k):.15f}\n')

    def test_fprobability_2(self):
        k = 15
        self.assertAlmostEqual(0.999969482422, fprobability(k), places=12)
        print(f'expected vs got\n{0.999969482422:.12f}\n{fprobability(k):.12f}\n')

    def test_fprobability_3(self):
        k = 29
        self.assertAlmostEqual(0.999999998137, fprobability(k), places=12)
        print(f'expected vs got\n{0.999999998137:.10f}\n{fprobability(k):.10f}\n')


# Do auto answer match my by-hand ones?
class TestModularExponentiation(TestCase):

    def test_mod_exp_1(self):
        self.assertEqual(8, mod_exp(5, 3, 13))

    def test_mod_exp_2(self):
        self.assertEqual(1, mod_exp(5, 10, 6))

    def test_mod_exp_3(self):
        self.assertEqual(9, mod_exp(3, 2, 50))

    def test_mod_exp_4(self):
        self.assertEqual(445, mod_exp(4, 13, 497))

    def test_mod_exp_5(self):
        self.assertEqual(0, mod_exp(0, 5, 10))

    def test_mod_exp_6(self):
        self.assertEqual(1, mod_exp(5, 0, 10))

    def test_mod_exp_7(self):
        self.assertEqual(8, mod_exp(2, 21, 18))


# Were the answers given correct
class TestMillerRabinAccuracy(TestCase):

    def test_miller_rabin(self):
        self.fail()


# Testing the probability that Miller Rabin is going to give the correct answer
class TestMillerRabinProbability(TestCase):

    def test_mprobability(self):
        self.fail()
