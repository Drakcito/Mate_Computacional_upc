import sys
print("\n>>Encriptar o Desencriptar mensaje<<\n")
print("Ejemplo:\ncnum**(e)ó(d) mod (n)\n")
print("Clave privada: (n,d)")
print("Clave publica: (n,e)")
print('\nPara salir escriba "done"')

def exit_progrm():
    if n=="done" or e=="done" or num=="done":
        print("\nSaliendo del programa...")
        sys.exit()

i=0
while True:
    n=input("\nIngrese (n): ")
    try:
        fn=int(n)
        break
    except ValueError:
        exit_progrm()
        print("Invalid input. Please enter a valid(n) integer.")
    
while True:
    e=input("\nIngrese (e) o (d): ")
    try:
        fe=int(e)
        break
    except:
        exit_progrm()
        print("Invalid input. Please enter a valid(e)(d) integer.")
    
while True:
    num=input("\nIngrese variable(cnum): ")
    try:
        fnum=int(num)
    except:
        exit_progrm()
        print("Invalid input")
        continue
    rpta=fnum**fe % fn

    i+=1
    print(i,")",rpta)