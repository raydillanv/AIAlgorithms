from unittest import TestCase


class test(TestCase):
    def test_collatz(self):
        from week1 import collatz
        from week1 import biggest_seq
        from week1 import has_aaa
        from week1 import make_bunch
        self.assertEqual(collatz(12), 10)
        self.assertEqual(collatz(100), 26)
        self.assertEqual(collatz(1), 1)
        self.assertEqual(collatz(5), 6)
        self.assertEqual(collatz(7), 17)
        self.assertEqual(collatz(18), 21)
        self.assertEqual(biggest_seq(100000),(351, 77031))
        self.assertEqual(has_aaa("testString"), False)
        self.assertEqual(has_aaa("teststraaang"), True)
        self.assertEqual(has_aaa("teststrAAAng"), True)
        self.assertEqual(has_aaa("teststraang"), False)
        self.assertEqual(make_bunch(4,8,10,15), [3,0,6])
        self.assertEqual(make_bunch(3,8,10,19), [3,2,6])
        self.assertEqual(make_bunch(4,8,2,15), [])
        self.assertEqual(make_bunch(4,1,6,23), [])
        self.assertEqual(make_bunch(500,0,4,40), [])

