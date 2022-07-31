class Dog:
    def __init__(self, age_dog):
        self.age_dog = age_dog


    def age_human(self):
        fact = self.age_dog * 7
        print (f'Якщо собаці {self.age_dog} роки то на людський вік це {fact}')


about_age = Dog(2)
about_age.age_human()