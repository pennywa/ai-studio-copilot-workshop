"""
Exercise 1: Tab completion warm-up

None of the functions below do anything yet. Each one has a comment
describing what it should do and a `pass` placeholder instead of real
code.

For each function: delete the `pass` line, put your cursor there, and
start typing. Once GitHub Copilot is enabled, it will offer a suggestion as gray "ghost
text." Press Tab to accept it, Esc to dismiss it, or keep typing your
own version.
"""


def square(n):
    # Return the square of n.
    return n ** 2

'''
Returns n multiplied by itself (n squared).

n*n would also work. 

Question: under the hood, is there a difference between n**2 and n*n?
Answer: Yes, there is a difference in how they are executed.
- n**2 uses the exponentiation operator, which is a more general operation that can handle any exponent, not just 2. It may involve more overhead because it has to handle the general case of exponentiation.
- n*n is a simple multiplication operation, which is generally faster and more efficient for squaring a number. It directly multiplies n by itself without any additional overhead.

'''

def is_prime(n):
    # Return True if n is prime, False otherwise.
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
'''
# Numbers < 2 are not prime. For n >= 2, test divisors up to sqrt(n);
# if no divisor divides n evenly, n is prime.
'''

def filter_by_length(strings, min_length):
    # Return only the strings from `strings` that are at least
    # `min_length` characters long.
    return [s for s in strings if len(s) >= min_length]

'''Iterates through each string, checks if len(s) >= min_length, 
and collects matching strings into a new list.
'''

def reverse_sentence(sentence):
    # Reverse the word order of `sentence`.
    # "hello world" becomes "world hello".

    '''Copilot suggestion
    words = sentence.split()
    return ' '.join(reversed(words))
    '''
    return ' '.join(sentence.split()[::-1]) # more pythonic way to reverse the list of words

''' 
1. More concise.
2. Idiomatic slicing: [::-1] is standard Python shorthand for reversing any sequence (lists, strings, tuples).
3. Efficiency: sentence.split() generates a list directly in memory, so slicing it creates a reversed list in C-speed without requiring the overhead of an iterator object wrapper from reversed().

What is C-speed?
Basically it's: Python skipped the slow translation step and let the raw, ultra-fast engine underneath do the heavy lifting.

Regular Python speed: You write a manual Python for loop to inspect and move every single word one by one. The translator has to work on every single step.

C-speed: You use a built-in feature like words[::-1] or .split(). Python hands the entire job to a pre-built C routine behind the scenes. The C routine finishes the whole task directly in the CPU's native speed and just hands Python back the final result.

'''
