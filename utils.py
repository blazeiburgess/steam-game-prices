from random import randint, random
from time import sleep


def random_sleep(min_: int, max_: int):
    sleep_time = randint(min_,max_) + random()
    sleep(sleep_time)


