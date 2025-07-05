import time


def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("Total time taken by the function", end_time - start_time)

    return wrapper()


def Log_decorator(func):
    def wrapper():
        print("start the logs")
        func()
        print("end the logs")

    return wrapper()


@Log_decorator
@time_decorator
def test_ui1():
    print("Add function, time taken by this function1")
    time.sleep(2)


@time_decorator
def test_ui2():
    print("Add function, time taken by this function2")
    time.sleep(5)


test_ui1()
