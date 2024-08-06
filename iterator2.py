class MyIterator:
    def __iter__(self):
        self.a = 4
        print('Inside __Iter')
        return self
    def __next__(self):
        print('Inside Next')
        x = self.a
        self.a += 1
        return x

my_iter = MyIterator()
print('Before Calling')
it = iter(my_iter)
print(next(it))
print(next(it))
print(next(it))
