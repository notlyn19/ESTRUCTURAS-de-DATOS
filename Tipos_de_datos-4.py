# 4 seccion
#Tipos de Datos

"""
Tipo de texto:	str
Tipos numéricos:	int, float, complex
Tipos de secuencia:	list, tuple, range
Tipo de mapeo:	dict
Tipos de conjuntos:	set,frozenset
Tipo booleano:	bool
Tipos binarios:	bytes, bytearray, memoryview
Ninguno Tipo:	NoneType

"""
#complex 

x = complex(1j) 

print(x)
print(type(x)) 

#List 
#se puede modificar 

lista = list(("apple", "banana", "cherry"))

#display x:
print(lista)

#display the data type of x:
print(type(lista)) 


#tuple 
#no se puede modificar luego de creada, y se debe definir el tamaño, el cual no se puede modificar

x = tuple(("apple", "banana", "cherry"))

print(x)
print(type(x)) 

#set 
#no permite elementos duplicados, permite 



#range
"""
range(stop)
      range(start, stop)
      range(start, stop, step)

"""
i=0
for i in range(2, 9, 2):
          print(i)
        
         


#dict

 
thisdict = {"name" : "John", "age" : 36}

#display x:
print(thisdict)

#display the data type of x:
print(type(thisdict)) 

y = {"name" : "John", "age" : 36}

#display x:
print(y)

#display the data type of x:
print(type(y)) 
