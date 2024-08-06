class MyIterator:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

my_iter = MyIterator()
it = iter(my_iter)
print(next(it))
print(next(it))
print(next(it))
