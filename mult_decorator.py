from functools import wraps

def logging_decorator(func):
    @wraps(func)
    def wrapper():
        wrapper.count += 1
        print("{0} times".format(wrapper.count))
        print(wrapper)
        func()
    wrapper.count = 0
    return wrapper


def a_function():
    print("Im a simple function")

modified_function = logging_decorator(a_function)
print(modified_function.__name__)#__name__)
print(modified_function.__module__)
# modified_function()
# modified_function()
# modified_function()
# modified_function()
