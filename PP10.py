def input_check():  # обработчик ошибок ввода
    while True:
        try:
            a = int(input("Введите необходимую сумму: "))
            if a <= 0:
                print("Введите натуральное число!")
            else:
                return a
        except ValueError:
            print("Некоректное значение, попробуйте ещё раз")


n = input_check()
rem64 = n//64  # делим нацело, вычитаем, делима нацело что осталось и т.д.
n -= rem64 * 64
rem32 = n//32
n -= rem32 * 32
rem16 = n//16
n -= rem16 * 16
rem8 = n//8
n -= rem8 * 8
rem4 = n//4
n -= rem4 * 4
rem2 = n//2
n -= rem2 * 2
rem1 = n
print("Необходимо использовать купюры, номиналом:\n"
      f"По 64 - {rem64}\n"
      f"По 32 - {rem32}\n"
      f"По 16 - {rem16}\n"
      f"По 8 - {rem8}\n"
      f"По 4 - {rem4}\n"
      f"По 2 - {rem2}\n"
      f"По 1 - {rem1}")
