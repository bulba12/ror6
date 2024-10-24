result = []

def divider(a, b):
    if a < b:
        raise ValueError("a менше ніж b")
    if b > 100:
        raise IndexError("b більше ніж 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():
    try:
        res = divider(int(key), value)
        result.append(res)
    except ZeroDivisionError:
        print(f"Ділення на нуль для пари ({key}, {value})")
    except TypeError:
        print(f"Некоректний тип для ключа або значення: ({key}, {value})")
    except ValueError as e:
        print(f"Помилка значення для пари ({key}, {value}): {e}")
    except IndexError as e:
        print(f"Індекс помилка для пари ({key}, {value}): {e}")

print(result)
