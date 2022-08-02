

class Dog:
    def __init__(self, age_dog):
        self.age_dog = age_dog


    def age_human(self):
        fact_ = self.age_dog * 7
        print(fact_)
        return fact_

about_age = Dog(2)
about_age.age_human()


