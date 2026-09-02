from functools import wraps


def remember_last(func):
    """Декоратор, запоминающий результат последнего вызова функции."""
    last_args = None
    last_kwargs = None
    last_result = None
    has_result = False  
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal last_args, last_kwargs, last_result, has_result
        if has_result and args == last_args and kwargs == last_kwargs:
            return last_result
        result = func(*args, **kwargs)
        last_args = args
        last_kwargs = kwargs
        last_result = result
        has_result = True
        return result
    return wrapper
@remember_last
def slow_add(a, b):
    print("Функция реально считается...")
    return a + b


print(slow_add(2, 3))  
print(slow_add(2, 3))   
print(slow_add(2, 3))   
print(slow_add(4, 5))   
print(slow_add(4, 5))  
