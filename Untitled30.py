#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
labels = ['Apple','Banana','Cherry','Mango']
sizes=[30,25,20,25]
plt.pie (sizes,labels=labels,autopct='%1.1f%%',startangle=90)
plt.title('Fruit distribution')
plt.show()


# In[11]:


import matplotlib.pyplot as plt
labels= ['chrome','fire fox','edge','safari']
sizes = [65,20,10,5]
plt.pie (sizes,labels=labels,autopct='%1.1f%%',startangle=96)
plt.title ('browser usage' 'Distribution')
plt.show()


# In[18]:


import matplotlib.pyplot as plt

students = ['A', 'B', 'C', 'D']
marks = [78, 85, 90, 88]

plt.bar(students, marks, color='skyblue')

plt.title('Students marks Analysis')
plt.xlabel('Students')
plt.ylabel('marks')

plt.grid(axis='y') 

plt.show()


# In[ ]:




