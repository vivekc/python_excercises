from functools import wraps

count = 0


def logit(filename='tmp.log'):
    def logging_decorator(func):
        @wraps(func)
        def mylogger(*args, **kwargs):
            count = 0
            log_string = func.__name__ + "logging %count " % str(count)
            count += 1
            with open(filename, 'a') as openedfile:
                openedfile.write(log_string + "\n")
        return mylogger

    return logging_decorator


@logit(filename='temporary.log')
def mycalc():
    pass


@logit()
def mycalc2():
    pass


if __name__ == '__main__':
    mycalc()
    mycalc2()
