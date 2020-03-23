from randoms import mkm_rand
import random


class mac_mars_rand:
    def __init__(self, k, m1, a1, b1, c1, m2, a2, b2, c2):
        if m1 < m2:
            m1, m2 = m2, m1
        if m1 % m2 == 0:
            raise ArithmeticError('Invalid Periods! Check initial arguments!')
        self.k = k
        self.__gen_1 = mkm_rand(m1, a1, b1, c1)
        self.__gen_2 = mkm_rand(m2, a2, b2, c1)
        self.V = [self.__gen_1.next() for _ in range(self.k)]

    def next(self):
        s = random.randint(0, self.k - 1)
        res = self.V[s]
        self.V[s] = self.__gen_2.next()
        return res


if __name__ == '__main__':
    print('Testing random generators...')
    print('Random generator 3, creating 10000 nums...')
    generator_3 = mac_mars_rand(256, 64, 35, 9, 11, 123, 123, 124 * 3, 11)
    with open('output3.txt', 'w') as fout:
        for _ in range(1000):
            randint = generator_3.next()
            print(randint, file=fout)
            print('%.5f' % randint, end='\t' if _ % 100 != 0 else '\n')
    print('*********************************************************************************')
    print('Random generator 4, creating 1000 nums...')
    generator_4 = mac_mars_rand(256, 129, 262147, 2 * 3 * 7 * 13 * 983317 + 1, 17, 123, 123, 124 * 3, 11)
    with open('output4.txt', 'w') as fout:
        for _ in range(1000):
            randint = generator_4.next()
            print(randint, file=fout)
            print('%.5f' % randint, end='\t' if _ % 100 != 0 else '\n')





