import numpy as np

escalar = np.array(42)
print("Escalar: ",escalar)
print("Dimensiones escalar: ",escalar.ndim)

# Una dimension
vector = np.array([1,2,3])
print("Vector",vector)
print("Dimensiones vector: ",vector.ndim)

# Dos dimensiones
matriz = np.array([[1,2,3],[4,5,6]])
print("Matriz: ",matriz)
print("Dimensiones matriz: ",matriz.ndim)

# Mas de dos dimensiones
tensor = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("Tensor: ",tensor)
print("Dimensiones tensor: ",tensor.ndim)

# Agregar o eliminar dimensiones
vector = np.array([1,2,3],ndmin=10)
print("Vector: ",vector)
print("Dimensiones vector: ",vector.ndim)

# Expandir
expand = np.expand_dims(np.array([1,2,3]),axis=0)
print("Expand: ",expand)
print("Dimensiones expand: ",expand.ndim)

# Eliminar dimensiones que no se están usando
print("Vector a redimensionar: ",vector,"\nDimensiones del vector: ",vector.ndim)
vector2 = np.squeeze(vector)
print("Vector dimensionado: ",vector2)
print("Nuevas dimensiones: ",vector2.ndim)
