import os
import shutil

path = r"C:\Users\Andrea\Downloads"

source = r"C:\Users\Andrea\Documents\André"

destination = r"C:\Users\Andrea\Downloads\NÃO E DE AULA - AULA 102"

shutil.copy(origem, destino)
dest = shutil.copy(source, destination)

print(os.listdir(path))




#print("C:\Users\Andrea\Downloads") 
