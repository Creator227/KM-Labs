M1 = 64
M2 = 2147483648 + 8 * 10089
# 2147564360 = 2^3 * 3 * 7 * 13 * 983317    b = 2 * 3 * 7 * 13 * 983317 + 1  c = 17


class mkm_rand:
    def __init__(self, m: int, a: int, b: int, c: int):
        self.current = a
        self.m = m
        self.b = b
        self.c = c

    def next(self):
        self.current = (self.current * self.b + self.c) % self.m
        return self.current / self.m


if __name__ == '__main__':
    print('Testing random generators...')
    print('Random generator 1, creating 10000 nums...')
    generator_1 = mkm_rand(M1, 35, 9, 11)
    with open('output1.txt', 'w') as fout:
        for _ in range(1000):
            randint = generator_1.next()
            print(randint, file=fout)
            print('%.5f' % randint, end='\t' if _ % 64 != 0 else '\n')
    print('*********************************************************************************')
    print('Random generator 2, creating 1000 nums...')
    generator_2 = mkm_rand(M2, 262147, 2 * 3 * 7 * 13 * 983317 + 1, 17)
    with open('output2.txt', 'w') as fout:
        for _ in range(1000):
            randint = generator_2.next()
            print(randint, file=fout)
            print('%.5f' % randint, end='\t' if _ % 100 != 0 else '\n')
