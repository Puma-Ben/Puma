#!/usr/bin/env python
# coding: utf-8

# In[17]:


lista= [1,"hola",3.67, [1 , 2 , 3]]

print(lista [0:4])


# In[18]:


a=[90,"python",3.87]
print(a[-2])


# In[27]:


lista=[1,2]
lista.append(3)
print(lista)


# In[20]:


lista=[1,2]
lista.extend([3,4])
print(lista)


# In[37]:


lista=[1,3]
lista.insert(1,2)

print(lista)


# In[40]:


lista=[1,2,3]
lista.remove(2)
print(lista)


# In[44]:


lista=[1,2,3]
lista.pop(1)#si dejas el(vacio)se elimina el ultimo digito
print(lista)


# In[49]:


lista=[1,2,3]
lista.reverse()#aqui no puedes colocar nada
print(lista)


# In[53]:


lista=[11,23,9,432,764,2,6]
lista.sort()#ordena de menor a mayor, no lee letras ni decimales.
print(lista)


# In[55]:


lista=[11,23,9,432,764,2,6]
lista.sort(reverse=True)#ordena de mayor a menor, no lee letras ni decimales
print(lista)


# In[ ]:




