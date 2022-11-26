from colorama import init, Fore, Back, Style

def captura():
    num=int(input("Digite un numero"))
    return num

def factorial(num):
   res=1
   if(num==0):
        res=1
   else:
      for i in range(1,num+1):
        res=res*i
   return res

def mostrar1(n1, n2,sw):
    if (sw==1):
       print("El mayor de : ",n1, " y ", n2," es: ",n1)
    else:
        if(sw==2):
            print(n1, " y ", n2," son iguales")
        else:
            print("El mayor de : ",n1, " y ", n2," es: ",n2)


def mostrar(num,res):
   print("El factorial de: ",num, " es: ",res)

def captura1():
   mdo=int(input("Digite cuantas tablas desea"))
   return mdo

def captura2():
   mdor=int(input("Hasta dónde desea multipliar cada tabla"))
   return mdor

def captura3():
   mdo=int(input("Digite un número\t"))
   return mdo

def captura4():
   mdor=int(input("Digite otro número\t"))
   return mdor

def tablas(mdo, mdor):
   for i in range(1,mdo+1):
       print("Tabla del",i)
       for j in range(1,mdor+1):
          print(i," * ",j," = ",i*j)

def tablasVersion():
    print(Fore.GREEN+"+--------------------+----------+----------+-----------+")
    print(Fore.GREEN+"|                   TABLAS DE MULTIPLICAR              |")
    print(Fore.GREEN+"+----------+----------+----------+----------+----------+")
    print(Fore.GREEN+"|    1x    |    2x    |    3x    |    4x    |    5x    |")
    print(Fore.GREEN+"+----------+----------+----------+----------+----------+")
    x1,x2,x3,x4,x5=1,2,3,4,5
    x6,x7,x8,x9,x10=6,7,8,9,10
    for j in range(10):
        j+=1
        t1="1x"+str(j)+"="+str(x1*j)
        t2="2x"+str(j)+"="+str(x2*j)
        t3="3x"+str(j)+"="+str(x3*j)
        t4="4x"+str(j)+"="+str(x4*j)
        t5="5x"+str(j)+"="+str(x5*j)
        for v in range(1):
            cadena = "|{:>10}|{:>10}|{:>10}|{:>10}|{:>10}|".format(t1,t2,t3,t4,t5)
            print(Fore.BLUE+cadena)
            #print(Fore.GREEN+cadena[0]+Fore.BLUE+cadena[1:11]+Fore.GREEN+cadena[11:12]+Fore.BLUE+cadena[13:23]+Fore.GREEN+cadena[23:33]+Fore.BLUE+cadena[33:44]+Fore.GREEN+cadena[44:46]+Fore.BLUE+cadena[46:55]+Fore.GREEN+cadena[55:65]+Fore.BLUE+cadena[65:75]+Fore.GREEN+cadena[75:85])
        t1,t2,t3,t4,t5=1,1,1,1,1
        j-=1
    print(Fore.GREEN+"+----------+----------+----------+----------+----------+")
    print(Fore.GREEN+"|    6x    |    7x    |    8x    |    9x    |    10x   |")
    print(Fore.GREEN+"+----------+----------+----------+----------+----------+")
    for j in range(10):
        j+=1
        t1="6x"+str(j)+"="+str(x6*j)
        t2="7x"+str(j)+"="+str(x7*j)
        t3="8x"+str(j)+"="+str(x8*j)
        t4="9x"+str(j)+"="+str(x9*j)
        t5="10x"+str(j)+"="+str(x10*j)
        for v in range(1):
            cadena = "|{:>10}|{:>10}|{:>10}|{:>10}|{:>10}|".format(t1,t2,t3,t4,t5)
            print(Fore.BLUE+cadena)
        t1,t2,t3,t4,t5=1,1,1,1,1
        j-=1
    print(Fore.GREEN+"+----------+----------+----------+----------+----------+")
    exit()    

def maymin(n1,n2):
    if(n1>n2):
      sw =1
    elif(n1==n2):
      sw=2
    else:
        sw=3
    return sw

def salir():
    print("CHAO")

def error():
    print("Opción errada")

def menu():
   opc=1
   while(opc!=4):
    print("Opweraciones")
    print("============")
    print("1. Factorial")
    print("2. Tablas")
    print("3. Mayor o menor")
    print("4. Salir")
    opc=int(input("Digite su opción"))
    match(opc):
        case 1: 
                num=captura()
                res=factorial(num)
                mostrar(num,res)
        case 2: 
                mdo=captura1()
                mdor=captura2()
                tablas(mdo,mdor)
        case 3: 
                n1=captura3()
                n2=captura4()
                sw=maymin(n1,n2)
                mostrar1(n1,n2,sw)
        case 4: 
                salir()
        case other:
                error()

#bloque principal
#menu()
if __name__=='__main__':
    tablasVersion()