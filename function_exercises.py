#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.


# In[1]:


def is_two(x):
    if x == (2 or '2'):
         return(True)
    else:
         return(False)

is_two(3)


# In[ ]:


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.


# In[38]:


def is_vowel(x):
    vowel_letters =['a', 'e', 'i','o', 'u']
    if x.lower() in vowel_letters :
         return(True)
    else:
         return(False)

is_vowel('a')


# In[ ]:


# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.


# In[43]:


def is_consonant(x):
    vowel_letters =['a', 'e', 'i','o', 'u']
    if x.lower() not in vowel_letters :
         return(True)
    else:
         return(False)
        
is_consonant('d')
        
        


# In[ ]:


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.


# In[58]:


def word(dog):
    if is_consonant(dog[0]):
        return(dog.title())
    else:
        return(dog)
word('giraffe')


# In[ ]:


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.


# In[65]:


def calculate_tip(percent, total):
    return (percent * total)
calculate_tip(0.2, 50)


# In[ ]:


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.


# In[68]:


def apply_discount(original_price, discount_percentage):
    return (original_price -(original_price * discount_percentage))
apply_discount(100, 0.4)


# In[ ]:


# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.


# In[7]:



def handle_commas(number):
    delete_commas= number.replace(',', '')
    return int(delete_commas)
handle_commas('50,00,000')


# In[ ]:


# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).


# In[17]:


def letter_grade(number):
    if number >= 90:
        return 'A'
    elif number >= 80:
        return 'B'
    elif number >= 70:
        return 'C'
    elif number >= 60:
        return 'D'
    else:
        return 'F'
letter_grade(90)


# In[ ]:


# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.


# In[40]:


# 9
def remove_vowels(string):
    string2 = ""
    for char in string:
        if char not in 'aeiou':
            string2 += char
    return string2
remove_vowels ('hippoppotamus')


# In[41]:


# OR
def remove_vowels(vowels):
    for i in vowels:
        if i in 'a e i o u':
            return vowels.replace(i,'')
remove_vowels('dogdogdogdogdog')


# In[ ]:


# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become 'name'
# First Name will become 'first_name'
# % Completed will become 'completed'


# In[63]:


import re

def normalize_name(name):
    name = re.sub('\W|^(?=\d)','',name)
    name = name.strip()
    name = name.lower()
    name = name.replace(' ', '_')
    return(name)


# In[68]:


normalize_name('% /\?FINALLYdoNe^=')


# In[ ]:


# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]


# In[69]:


import numpy as np
a = [1,1,1]
np.cumsum(a)


# In[70]:


import numpy as np
a = [1,2,3,4]
np.cumsum(a)


# In[72]:


# OR
lis = [1,1,1]
from itertools import accumulate
list(accumulate(lis))


# In[73]:


lis = [1,2,3,4]
from itertools import accumulate
list(accumulate(lis))

