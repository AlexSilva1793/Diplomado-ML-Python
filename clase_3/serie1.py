import pandas as pd # Importacion estandar de la libreria Pandas
import numpy  as np # Importacion estandar de la libreria NumPy

# Crear diferentes tipos de datos
labels = ['a','b','c'] # lista de eetiquetas
my_list = [10,20,30] # lista con valores
arr = np.array([10,20,30]) # Convertir ista de valores en arreglo NumPy
d = {'a':10,'b':20,'c':30} # Creacion de un diccionario
#*Desde Listas
# Convertir una lista en series usando el metodo pd.Series
# observe que se crean los nombres con las posiciones de cada elemento
print(pd.Series(data=my_list))
# Convertir una lista en series usando el metodo pd.Series
# se puede ingresar el nombre de las posiciones
print(pd.Series(data=my_list,index=labels))
# No es necesario ingresar la palabra de 'data =''  en el argumento
print(pd.Series(my_list,labels))
#*Desde Arreglos NumPy
# Convertir un arreglo en series usando el metodo pd.Series
print(pd.Series(arr))
# Convertir un arreglo en series indicando tambien los valores del index
pd.Series(arr,labels)
#*Desde un Diccionario
# Convertir un diccionario en series usando el metodo pd.Series
# Como el diccionario ya tiene clave entonces se le asigna como valor de la posicion
print(pd.Series(d))
# Creando una serie basado solo en una lista de letras
print(pd.Series(data=labels))

# Creacion de una serie con sus labels o indices
ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])                                   
print(ser1)
# Creacion de una serie con sus labels o indices
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])                                   
# La busqueda en una serie es igual como en un diccionario
print(ser1['USA'])
# La busqueda en una serie es igual como en un diccionario
print(ser2['Germany'])
# unión de dos series
print(ser1 + ser2)