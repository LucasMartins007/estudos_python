

tabuada=int(input("Digite um número para que possa ser calculado "))

if tabuada > 0 and tabuada < 11:

 for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )
 
else:
      print('Esse número não é válido para essa operação')  


      