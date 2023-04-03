# do not change anything just enter your age

type_age = input("Enter your age ")

remaining_life = 90 - int(type_age)
days = 365 * remaining_life
weeks = 52 * remaining_life
months = 12 * remaining_life

print(f"you have {days} days, {weeks} weeks, {months} left to live your life")