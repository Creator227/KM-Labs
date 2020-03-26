M1 = 64
M2 = 1048576 + 8 * 10079
#    1048576 + 8 * 10079 = 1 129 208 = 2^3 * 17 * 19^2 * 23;‬
#    b =  2 * 17 * 19 * 23 + 1 = 14859;
#    c = 29

# Логика параметров следующая: b-1 кратно любому делителю M, а C взаимно простое с M.


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
    generator_2 = mkm_rand(M2, 262147, 14859, 29)
    with open('output2.txt', 'w') as fout:
        for _ in range(1200000):
            randint = generator_2.next()
            print(randint, file=fout)
            print('%.5f' % randint, end='\t' if _ % 100 != 0 else '\n')
    print('Random generator 3, creating 1000 nums...')
    generator_3 = mkm_rand(135, 234, 16, 19)
    for _ in range(1200000):
        randint = generator_2.next()
        print(randint, file=fout)
        print('%.5f' % randint, end='\t' if _ % 100 != 0 else '\n')
