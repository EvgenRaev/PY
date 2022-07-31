class Self:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age


    def get_d_mame(self):
        print(f" Hello, my name is {self.name} {self.lastname}, and I’m {self.age} years old")

about_self = Self("Carl", "Johnson ", "26")
about_self.get_d_mame()



class Dog:
    def __init__(self, age_dog):
        self.age_dog = age_dog


    def age_human(self, fact):
        fact = self.age_dog * 7
        return fact

about_age = Dog("2")
about_age.age_human()
