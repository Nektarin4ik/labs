from string import digits



def main():
    number=get_number()
    meow(number)

def get_number():
    while True:
        number = int(input('Введите число?'))
        if number >0:
            break
    return number

def meow(number):
    for i in range(number):
        print('meow')


class film():
    product_c='cinema'
    def __init__(self, universe):
        self.universe = universe

#Банковский счет, который можно пополнять и с которого можно снимать деньги

class BankAccount():

    def __init__(self, name, balance):
        self.name=name
        self.__balance=balance
    
    @property
    def my_balance(self):
        print('get balance')
        return self.__balance

    #my_property_balance=my_balance
    @my_balance.setter
    def my_balance(self, value):
        if value < 0:
            print('Снятие денег с депозита')
            if self.__balance + value < 0:
                raise ValueError('Недостаточно средств')
            self.__balance = self.__balance + value
            return self.__balance
        print('Внесение денег на депозит')
        self.__balance=self.__balance + value



    #my_balance=my_property_balance.setter(my_balance)

a=BankAccount('Ivan', 300)

print(a.my_balance)
a.my_balance = 650

print(a.my_balance)

a.my_balance =-400

print(a.my_balance)

#Периметр прямоугольника (геттеры и сеттеры как свойство)

class Rectangle():
    def __init__(self, a, b):
        self.__f_side=a
        self.__s_side=b
        self.per=None

    @property
    def side1(self):
        return self.__f_side
    
    @side1.setter
    def side1(self,value1):
        self.__f_side=value1
        self.per=None

    @property
    def side2(self):
        return self.__s_side
    
    @side2.setter
    def side2(self,value2):
        self.__s_side=value2
        self.per=None

    @property
    def perimetr(self):
        if self.per is None:
            print('calculate')
            self.per = self.__f_side*2+self.__s_side*2
        return self.per



#Класс пользователь с проверкой пароля по критериям и секретным словом

default_pass=[
'1234567',
'1234567890',
'000000',
'qwertyuiop',
'123321',
'1234',
'abc123',
'654321',
'666666',
'1q2w3e4r5t',
'7777777',
'password1',
'iloveyou',
'555555',
'123',
'qwerty',
'123456',
'123456789',
'qwerty',
'12345',
'password',
'12345678',
'qwerty123',
'1q2w3e',
'111111',
'123123']


class User():

    def __init__(self, login, password):
        self.login=login
        self.password=password
        self.__secret_key='Nektarin4ik'

    @property
    def secret_key(self):
        s = input('Введите ваш пароль: ')
        if s==self.password:
            return self.__secret_key
        else:
            raise ValueError ('Доступ закрыт')

    @property
    def password(self):
        print('getter called')
        return self.__password
    
    @staticmethod
    def check_default_pass(password):
        #print(f'get check {password}')
        if password in default_pass:
            return True
        return False

    @staticmethod
    def check_number_in_password(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError('Пароль должен быть строкой')
        if len(value) < 8:
            raise ValueError('Пароль слишком короткий, минимум 8 символов')
        if not User.check_number_in_password(value):
            raise ValueError('Должен содержать в себе цифры')
        if User.check_default_pass(value):
            print('check', User.check_default_pass(value))
            raise ValueError('Пароль слишком простой')
        print('setter called')
        self.__password=value

# a=User('Nektarin4ik', 'password123')

# print (a.password)

# a.secret_key

