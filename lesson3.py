class Human:
    def __init__(self, name, age):
        self.name=name
        self.age=age

class Prince(Human):
    def __init__(self, name, age, size_prince):
        super().__init__(name,age)
        self.size_prince=size_prince
    def __str__(self):
        return f'{self.name}+{self.size_prince}'
    def __repr__(self):
        return f'{self.name}+{self.size_cnd}'

    def chosen_cinrderella( self, others):
        for i in others:
            print(f'{i.name}  {self.size_prince}')
            if (i.size_cnd==self.size_prince):
                print(f'{i.name} cinderella size {i.size_cnd} and {self.name} prince {self.size_prince}')


class Cinderella(Human):
    def __init__(self, name, age, size_cnd):
        super().__init__(name,age)
        self.size_cnd=size_cnd
    def __str__(self):
        return f'{self.name}+{self.size_cnd}'
    def __repr__(self):
        return f'{self.name}+{self.size_cnd}'

pr1=Prince("juy", 25, 40)
c1=Cinderella("nh", 40, 40)
c2=Cinderella("ll",25, 10)
c=[c1, c2]
pr1.chosen_cinrderella(c)

