"""
Exercise 2: Explain and fix a bug with Copilot Chat

The function below is real, runnable code. It computes the average of
a list of numbers, but it has a bug.

1. Select the `average` function, including the def line.
2. Open Copilot Chat and ask it to explain what the function does.
3. Run this file. Watch the second call crash.
4. Ask Copilot Chat why the crash happens, then ask it to fix the
   function. Read the fix before you accept it. Does it handle an
   empty list the way you would want it to?
"""


def average(numbers):
    if not numbers:
        raise ValueError("average of an empty list is undefined")

    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


print(average([1, 2, 3, 4, 5]))
print(average([]))

'''
More "elegant" way:

def average(numbers):
    if not numbers:
        raise ValueError("average of an empty list is undefined")
    return sum(numbers) / len(numbers)   
'''


'''
What the function does
The function average(numbers) calculates the arithmetic mean of a list of numbers.

It works like this:

starts with total = 0
loops through each value in numbers
adds each value to total
after the loop, returns total / len(numbers)

So for example:

average([1, 2, 3, 4, 5]) becomes:
total = 1 + 2 + 3 + 4 + 5 = 15
len(numbers) = 5
result = 15 / 5 = 3.0

The bug
It crashes when numbers is an empty list:

len([]) is 0
so it does total / 0
which raises a ZeroDivisionError
This is the reason the second print in your file fails.
'''

'''
✅ Fix applied
I updated the function so it handles an empty list explicitly:

if the list is empty, it raises a clear ValueError
otherwise it calculates the average as normal.

This prevents the ZeroDivisionError and makes the failure explicit and intentional.

This is usually the safest behavior for an average: an empty list has no defined mean, so raising a clear exception is better than silently returning a nonsense value.

If you want, I can also show the “best” version using Python’s built-in sum() and explain why it’s cleaner.
'''

'''
What sum() does
sum() is a built-in Python function that adds up all the numbers in an iterable, like a list.

Example:
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)   # 15

It works by doing this internally:
total = 0
for n in numbers:
    total += n

So in your average function can be simplified to:
total = sum(numbers)

Then the average becomes:
return sum(numbers) / len(numbers)

'''