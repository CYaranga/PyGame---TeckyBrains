mascotas = ['perro', 'gato', 'perro', 'goldfish', 'gato', 'conejo', 'gato']
print(mascotas)

# while mascotas:
#     print(mascotas.pop(-1))
        
# for mascota in mascotas:
#     print(mascota)

index = 0
while index < mascotas.__len__():
    print(mascotas[index])
    index += 1

print(mascotas)