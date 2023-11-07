
# task -> https://youtu.be/yDzmx4HGJWA
# Підсказка: Щоб отримати довжину елемента(строки) використовуй ->   len(element)

def filter_strings_length_5_or_less(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        filtered_result = [x for x in result if len(x) <= 5]
        return filtered_result
    return wrapper

lst = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

@filter_strings_length_5_or_less
def my_function(lst: list):
    return lst

result = my_function(lst)
print(result)
