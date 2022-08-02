class Mathematician:
    def lists(self, m):
        self.m = m

    def square_nums(self, x):
        self.x = list(x)
        for a in x:
            xx = [a**2 for a in x]

        return xx

    def remove_positives(self, x):
        self.x = list(x)

        for a in x:
            if a > 0:
                x.remove(a)
        return x

    def filter_leaps(self, x):
        self.x = list(x)
        years_v = []
        for year in x:
             if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                years_v.append(year)

        return years_v



m = Mathematician()
print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]