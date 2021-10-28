class Lab1:

    def pedirNumeroPositivo(self, mensaje):
      datoValido = False
      while (datoValido == False):
          try:
              numero = int(input(mensaje))
              if (numero < 0):
                  print("Por favor ingrese valores positivos.")
              else:
                  datoValido = True
          except:
              print("Por favor ingrese valores válidos.")
      return numero
  
    def carne(self):
        carne = self.pedirNumeroPositivo("Por favor ingrese el numero de carne: ")
        iterador = self.pedirNumeroPositivo("Por favor ingrese el valor del iterador: ")
        char = input("Por favor ingrese un caracter: ")
        carne1 = carne % 2
        if carne1 == 1:
            for i in range(1,iterador+1):
                print(" ")
                for j in range(1,i+1):
                    print(char, end=" ")
        if carne1 == 0:
            for i in range(iterador,0,-1):
                print(" ")
                for j in range(1,i+1):
                    print(char, end=" ")
                
            
                

  
    
    def controlador(self):
        self.carne()
  
    
miInst = Lab1()
miInst.controlador()
