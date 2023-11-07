from typing import Callable
import time

end_range = 99999999

# task -> https://youtu.be/eo0oVdaqUPQ

def func_trigger(func: Callable) -> None:
    def wrapper(*args, **kwargs) -> list:
        start = time.time()
        print(f"Функція під назвою {func.__name__} була запущена")
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Час виконання функції {round(end-start, 2)} секунд")
        return result

    return wrapper


@func_trigger
def func_to_decor(end_range: int) -> list:
    return [num for num in range(1, end_range)]

func_to_decor(end_range)
