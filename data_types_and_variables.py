#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 1 You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?


# In[7]:


Rental_movies = [('Little Mermaid',3), ('Brother Bear', 5), ('Hercules', 1)]


# In[8]:


print('Total rental movies cost:' + str((movies[0][1] + movies[1][1] + movies[2][1])*3))


# In[ ]:


# 2 Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.


# In[9]:


Total_work_week = [('Google', 400, 6),('Amazon', 380, 4), ('Facebook', 350, 10)]


# In[14]:


Total_pay = (Total_work_week[0][1]*Total_work_week[0][2]) + (Total_work_week[1][1]*Total_work_week[1][2]) + (Total_work_week[2][1]*Total_work_week[2][2])


# In[15]:


print(Total_pay)


# In[ ]:


# 3 A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.


# In[23]:


If_class_full = False


# In[24]:


If_schedule_conflict = False


# In[25]:


class_enroll_ok = not If_class_full and not If_schedule_conflict


# In[28]:


print(class_enroll_ok)


# In[1]:


# 4 A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.


# In[2]:


people_buys = 3


# In[4]:


offer_expires = False 


# In[6]:


A_product_offer = (people_buys > 2) and not offer_expires


# In[7]:


print(A_product_offer)


# In[ ]:




