#decimal-  binario 
decimal = int(input("Ingrese un numero decimal: "))
print (type(decimal))
binario= bin(decimal)[2: ]
print (binario)
octal =(oct(decimal)[2: ])
print(f"octal = {octal}")
hexadecimal =(hex(decimal)[2: ])
print(f"hexadecimal = {hexadecimal.upper()}")