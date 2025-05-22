def fib(n):
# F(0) = 0
# F(1) = 1
# Упрощенная проверка
    if n < 2:
        return n
    else:
# Рекурсия - наивная реализация
# F(n) = F(n - 1) + F(n - 2)
        return fib(n-1) + fib(n-2)

import time
# Заголовок таблицы для англоязычного Excel
# print("n,T")
# Заголовок таблицы для русскоязычного Excel
print("n;T")
for n in range(35):
    start = time.time()
    fib(n)
    end = time.time()
    tn = end - start
    # Выводим на экран - CSV для англоязычного Excel
    # print(f"{n},{tn:.10f}")
    # Выводим на экран - CSV для русскоязычного Excel
    # Разделитель полей - точка с запятой
    # Десятичный разделитель - запятая
    print(f"{n},{tn:.10f}".replace(",",";").replace(".",","))
# Запускаем с перенаправлением в файл *.CSV
# python fibonacci_recursion.py > fibonacci_recursion.csv

# (cc) Арьков В.Ю.
