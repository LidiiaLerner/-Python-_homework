__author__ = 'Lerner Lidiia'

# Задание-5:
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceed = int(input("Enter proceed: "))
outlay = int(input("Enter outlay: "))
if proceed > outlay:
    profitability = proceed-outlay
    rent = profitability/proceed
    print(f"Great work. You have {profitability} profitability")
    worker = int(input("How many people work: "))
    print(f"{profitability/worker} for one worker")
elif proceed == outlay:
    print("No bad")
else:
    print("Good luck")