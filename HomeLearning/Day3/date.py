#Question: https://ww2.cs.fsu.edu/~dennis/teaching/2017_fall_cop3330/assignments/p2/assign2.pdf

month_abb = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr', '5': 'May', '6': 'June', '7': 'July', '8': 'Aug', '9': 'Sept', '10': 'Oct', '11': 'Nov', '12': 'Dec'}

class Date():
    def __init__(self, m = 1, d = 1, y = 2000) -> None:
        self.get_month(m)
        self.get_day(d)
        self.get_year(y)
        self.set_date(m, d, y)
        self.__user_date = f'{self.m}/{self.d}/{self.y}'

    def get_input(self):
        self.__user_date = input('Enter a date following format month/day/year: ')
        date_as_list = self.__user_date.split('/')
        self.m = int(date_as_list[0])
        self.d = int(date_as_list[1])
        self.y = int(date_as_list[2])
        if self.set_date(self.m, self.d, self.y) is False:
            print('Invalid date. Try again.')
            self.get_input()

    def get_month(self, m):
        self.m = int(m)
        return self.m

    def get_day(self, d):
        self.d = int(d)
        return self.d
    
    def get_year(self, y):
        self.y = int(y)
        return self.y
    
    def set_date(self, m, d, y):
        self.get_month(m)
        self.get_day(d)
        self.get_year(y)
        self.__handle_leap_yr()
        if self.m > 12 or self.m < 1 or self.d < 1 or (self.m in [1,3,5,7,8,10,12] and self.d > 31) or (self.m == 2 and self.d > self.__feb_days) or (self.m not in [1,2,3,5,7,8,10,12] and self.d > 30) or self.y < 0:
            self.m = 1
            self.d = 1
            self.y = 2000
            self.__user_date = f'{self.m}/{self.d}/{self.y}'
            return False
        self.__user_date = f'{self.m}/{self.d}/{self.y}'
        return True

    def set_format(self, setting_code = 'D'):
        if setting_code == 'D':
            self.__user_date = f'{self.m}/{self.d}/{self.y}'
        elif setting_code == 'T':
            if self.m in range(10):
                self.m = '0' + str(self.m)
            if self.d in range(10):
                self.d = '0' + str(self.d)
            self.__user_date = f'{self.m}/{self.d}/{str(self.y)[-2:]}'
        elif setting_code == 'L':
            self.__user_date = f'{month_abb[str(self.m)]} {self.d}, {self.y}'
        elif setting_code == 'J':
            self.__set_jul_days()
            self.__user_date = f'{str(self.y)[-2:]}-{self.__jul_days}'
        else:
            return False
        return True

    def increase_days(self, num_days = 1):
        self.__handle_leap_yr()
        if self.m == 12 and self.d == 31:
            self.y += 1
            self.m = 1
            self.d = num_days
        elif self.m in [1,3,5,7,8,10] and self.d == 31:
            self.m += 1
            self.d = num_days
        elif self.m == 2 and self.d == self.__feb_days:
            self.m = 3
            self.d = num_days
        elif self.m not in [1,2,3,5,7,8,10,12] and self.d == 30:
            self.m += 1
            self.d = num_days
        else:
            self.d += num_days
        self.__user_date = f'{self.m}/{self.d}/{self.y}'

    def compare(self, other_date):
        if self.y == other_date.y:
            if self.m == other_date.m:
                if self.d == other_date.d:
                    return 0
                elif self.d > other_date.d:
                    return 1
                else:
                    return -1
            elif self.m > other_date.m:
                return 1
            else:
                return -1
        elif self.y > other_date.y:
            return 1
        else:
            return -1

    def show(self):
        print('Date is:', self.__user_date)
    
    def __handle_leap_yr(self):
        if str(self.y)[-2:] != '00':
            if self.y % 4 == 0:
                self.__feb_days = 29
            else:
                self.__feb_days = 28
        else:
            if self.y % 400 == 0:
                self.__feb_days = 29
            else:
                self.__feb_days = 28
    
    def __set_jul_days(self):
        self.__handle_leap_yr()
        days_in_month = {'1': 31, '2': self.__feb_days, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
        self.__jul_days = 0
        for i in range(self.m-1):
            self.__jul_days += days_in_month[str(i+1)]
        self.__jul_days += self.d
        if self.__jul_days < 100:
            self.__jul_days = '0' + str(self.__jul_days)

d1 = Date(10, 1, 1998)
d1.set_format('J')
d1.show()