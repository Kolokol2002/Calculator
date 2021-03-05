import datetime as dt

class Record:
    def __init__(self, amount, comment, date=' '):
        self.amount = amount
        self.comment = comment
        self.date = date

        if self.date == ' ': #.strptime('%d.%m.%Y')
            now = dt.datetime.now()
            self.date = now.strftime('%d.%m.%Y')


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        limit = self.limit
        amount_date = []
        date = []
        for a in range(len(self.records)):
            limit -= self.records[a].amount
        for d in range(len(self.records)):
            date.append(self.records[d].date)

        amount_date.append(limit)
        amount_date.append(date)

        return amount_date

    def get_week_stats(self):
        spended = self.get_today_stats()[0]
        date = self.get_today_stats()[1]
        return f'За тиждень витрачено {spended}'

class CashCalculator(Calculator):
    UAN_RATE = 1
    USD_RATE = 27.68
    EURO_RATE = 33.27
    def __init__(self, limit,):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        spend = self.get_today_stats()[0]
        if spend < self.limit and spend > 0:
            return f'На сегодня осталось {spend} {currency}'
        elif spend == 0:
            return f'Денег нет, держись'
        elif spend < 0:
            return f'Денег нет, держись: твой долг - {abs(spend)} {currency}'

class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        spend = self.get_today_stats()[0]
        if spend < self.limit and spend > 0:
            return f'На сегодня осталось {spend} калорий'
        elif spend == 0:
            return f'Лимит калорий исчерпан'
        elif spend < 0:
            return f'Лимит калорий исчерпан: ты сел на {abs(spend)} калорий больше'



cash_calculator = CashCalculator(1000)
calories_calculator = CaloriesCalculator(500)

cash_calculator.add_record(Record(amount=0, comment="Серёге за обед"))
cash_calculator.add_record(Record(amount=2000, comment="бар в Танин др", date="08.11.2019"))
calories_calculator.add_record(Record(600, 'снікерс'))

print(calories_calculator.get_calories_remained())

лалал

ще шос

лол
