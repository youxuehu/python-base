class User:

    def hel(self):
        print('hello python')
        return 'hello python'

    def __init__(self, a, b, c):
        self.A = a
        self.B = b
        self.C = c


user = User(1, 2, 3)
print(user.A)
user.hel()
