#Question: https://ww2.cs.fsu.edu/~dennis/teaching/2017_fall_cop3330/assignments/p2/assign2.pdf

month_abb = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr', '5': 'May', '6': 'June', '7': 'July', '8': 'Aug', '9': 'Sept', '10': 'Oct', '11': 'Nov', '12': 'Dec'}

class Date():
    def __init__(self, m, d, y) -> None:
        if not self.set(m, d, y):
            print('Invalid date.')
            self.m = 1
            self.d = 1
            self.y = 2000
        self.__format_setting = 'Default'

    def get_input(self):
        input_date = input('Enter a date following format month/day/year: ')
        date_as_list = input_date.split('/')
        while not self.set(int(date_as_list[0]), int(date_as_list[1]), int(date_as_list[2])):
            input_date = input('Invalid date. Try again: ')
            date_as_list = input_date.split('/')
        self.m = int(date_as_list[0])
        self.d = int(date_as_list[1])
        self.y = int(date_as_list[2])

    def get_month(self):
        return self.m

    def get_day(self):
        return self.d
    
    def get_year(self):
        return self.y
    
    def set(self, m, d, y):
        if not self.__is_valid_day(m, d, y) or not self.__is_valid_year(y):
            return False
        self.m = m
        self.d = d
        self.y = y
        return True

    def set_format(self, code):
        if code == 'D':
            self.__format_setting = 'Default'
        elif code == 'T':
            self.__format_setting = 'Two-Digit'
        elif code == 'L':
            self.__format_setting = 'Long'
        elif code == 'J':
            self.__set_jul_days(self.y)
            self.__format_setting= 'Julian'
        else:
            return False
        return True

    def increase_days(self, num_days = 1):
        for day in range(num_days):
            if self.m == 2:
                if (self.__is_leap_yr(self.y) and self.d == 29) or (not self.__is_leap_yr(self.y) and self.d == 28):
                    self.m = 3
                    self.d = 0
            elif self.d == 31:
                if self.m == 12:
                    self.y += 1
                    self.m = 1
                    self.d = 0
                elif self.m in [1,3,5,7,8,10]:
                    self.m += 1
                    self.d = 0
            elif self.d == 30:
                if self.m in [4,6,9,11]:
                    self.m += 1
                    self.d = 0
            self.d += 1

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
        if self.__format_setting == 'Default':
            string_date = f'{self.m}/{self.d}/{self.y}'
        elif self.__format_setting == 'Two-Digit':
            if self.m in range(10):
                self.m = '0' + str(self.m)
            if self.d in range(10):
                self.d = '0' + str(self.d)
            string_date = f'{self.m}/{self.d}/{str(self.y)[-2:]}'
        elif self.__format_setting == 'Long':
            string_date = f'{month_abb[str(self.m)]} {self.d}, {self.y}'
        elif self.__format_setting == 'Julian':
            if self.__jul_days < 100:
                if self.__jul_days < 10:
                    self.__jul_days = '00' + str(self.__jul_days)
                else:
                    self.__jul_days = '0' + str(self.__jul_days)
            string_date = f'{str(self.y)[-2:]}-{self.__jul_days}'
        print('Date:', string_date)

    def __is_valid_year(self, y):
        if y < 0:
            return False
        return True
    
    def __is_valid_month(self, m):
        if m > 12 or m < 1:
            return False
        return True

    def __is_valid_day(self, m, d, y):
        if not self.__is_valid_month(m):
            return False
        else:
            if d in range(1, 32):
                if m in [1,3,5,7,8,10,12]:
                    return True
                elif m in [4,6,9,11]:
                    if d != 31:
                        return True
                    return False
                else:
                    if d != 30 and d != 31:
                        if not self.__is_leap_yr(y):
                            if d != 29:
                                return True
                            return False
                        return True
                    return False
            return False

    def __is_leap_yr(self, y):
        if y % 400 == 0:
            return True
        elif y % 4 == 0:
            if y % 100 == 0:
                return False
        return False
    
    def __set_jul_days(self, y):
        if self.__is_leap_yr(y):
            feb_days = 29
        feb_days = 28
        days_in_month = {'1': 31, '2': feb_days, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
        self.__jul_days = 0
        for i in range(self.m-1):
            self.__jul_days += days_in_month[str(i+1)]
        self.__jul_days += self.d

d1 = Date(5, 17, 2023)
d1.set_format('J')
d1.show()