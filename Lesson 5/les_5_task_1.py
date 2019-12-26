# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import namedtuple

Company = namedtuple('Company', 'name, profit_1, profit_2, profit_3, profit_4, sum_')
number_enterprises = int(input('Введите колличество предприятий: '))
number_ = number_enterprises
company_new = []
while number_enterprises > 0:
    company = Company(
        input('Наименование предприятия: '),
        int(input('Прибыль за 1-й квартал? = ')),
        int(input('Прибыль за 2-й квартал? = ')),
        int(input('Прибыль за 3-й квартал? = ')),
        int(input('Прибыль за 4-й квартал? = ')),
        sum_=0
    )
    company = company._replace(sum_=sum([company.profit_1, company.profit_2, company.profit_3, company.profit_4]))
    company_new.append(company)
    number_enterprises -= 1

cp_sum = 0
for i in company_new:
    cp_sum += i.sum_

for i in company_new:
    if i.sum_ > cp_sum / number_:
        print(f'У предприятие {i.name} прибыль выше среднего')

for i in company_new:
    if i.sum_ < cp_sum / number_:
        print(f'У предприятие {i.name} прибыль ниже среднего')

# For много потому, что по условию задачи в начале нужно выводить предприятия у которой прибыль выше.
# если без разницы то этот код
# for i in company_new:
#     if i.sum_ > cp_sum / number_:
#         print(f'У предприятие {i.name} прибыль выше среднего')
#     elif i.sum_ < cp_sum / number_:
#         print(f'У предприятие {i.name} прибыль ниже среднего')
#