import time
import functools
import logging


from logger import setup_logger

bblogger = setup_logger("BBTreasureChest", level=logging.DEBUG)


def bb_result_test(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == False:
            bblogger.error(f"Test failed: {func.__name__}")
            pause = input("Press Enter to continue...")

        return result

    return wrapper


def bb_deprecated(reason: str, can_run: bool = False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # ! TODO uncomment this line
            # bblogger.warning(f"Function {func.__name__} is deprecated: {reason}")
            return func(*args, **kwargs) if can_run else None

        return wrapper

    return decorator


def execution_timer(func):
    """
    be careful with this since the return value is suppressed
    """

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        bblogger.info(f"Execution time: {end - start} seconds")
        execution_duration = end - start
        return execution_duration

    return wrapper


def test_timer():
    @execution_timer
    def test_function():
        time.sleep(2)

    print(test_function())  # 2.0000000000000004
