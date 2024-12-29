class Users:
    __instance = None
    def __new__(cls, *args, **kwargs):
        print('Я в нью')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        print('Я в ините')
        self.args = args
        for key, value in kwargs.items():
            setattr(self, key, value)
other = [1, 2, 3]
user ={'name': 'Vitas', 'age': 25, 'gender' : 'male'}

User1 = Users(*other, **user)
print(User1.args)
print(User1.name)
print(User1.age)
print(User1.gender)