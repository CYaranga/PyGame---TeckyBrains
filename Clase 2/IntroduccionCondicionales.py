lloviendo = input("Esta lloviendo? Si o No?").lower()

if lloviendo == "si":
  ##ocurre la primera linea de tiempo
  print("Abrigate!!!!")
  
elif lloviendo == "no se":
  #ocurre la segunda linea de tiempo
  print("ve a fijarte")
elif lloviendo == "tal vez":
  print("Hoy no sales!")
else:
  print("Puedes salir al parque")
# if lloviendo == "No":
#   print("Puedes salir al parque")