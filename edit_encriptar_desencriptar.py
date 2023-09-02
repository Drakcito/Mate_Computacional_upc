import sys

def validar_entrada(msg):
    while True:
        entrada=input(msg)
        try:
            value=int(entrada)
            return value
        except ValueError:
            if entrada=="done":
                print("\nSaliendo del programa...")
                sys.exit()
            else:
                print("Entrada invalida. Ingresa un entero.")
        
def calcular_resultado(msg,exponente,modulo):
    resultado=msg**exponente%modulo
    return resultado

print("\n>>Encriptar o Desencriptar mensaje<<\n")
print("Ejemplo:\ncnum**(e)ó(d) mod (n)\n")
print("Clave privada: (n,d)")
print("Clave publica: (n,e)")
print('\nPara salir escriba "done"')

modulo= validar_entrada("\nIngrese(n): ")
exponente= validar_entrada("\nIngrese(e) o (d): ")

i=0
while True:
   msg=validar_entrada("\nIngrese variable(msg): ")
   resultado=calcular_resultado(msg,exponente,modulo)
   
   i+=1
   print(i,")",resultado)
