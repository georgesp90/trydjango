# Create your tasks here

from __future__ import absolute_import, unicode_literals
from celery import shared_task
import random
from celery.decorators import task

print("whoop there it is ")
# @shared_task
# def add(x, y):
#     return x + y


# @shared_task
# def mul(x, y):
#     return x * y


# @shared_task
# def xsum(numbers):
#     return sum(numbers)

@task(name="sum_two_numbers")
def add(x, y):
 return x + y

@task(name="multiply_two_numbers")
def mul(x, y):
 total = x * (y * random.randint(3, 100))
 return total

@task(name="sum_list_numbers")
def xsum(numbers):
 return sum(numbers)