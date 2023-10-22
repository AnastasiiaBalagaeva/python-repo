money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month_budget = money_capital + salary
months = 0

while(month_budget >= 0):
    month_budget -= spend
    if (month_budget < 0):
        break
    spend *= 1 + increase
    months += 1
    month_budget += salary


print("Количество месяцев, которое можно протянуть без долгов:", months)
