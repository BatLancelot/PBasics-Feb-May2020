import datetime

birthday = input('Enter Your Birth Date /01-01-1900/: ')
birthday = datetime.datetime.strptime(birthday, '%d-%m-%Y')
t_delta = datetime.timedelta(days=1000)
after_1000_days = birthday + t_delta

print(after_1000_days.strftime('%d-%m-%Y'))
