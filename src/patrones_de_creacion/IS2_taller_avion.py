#*--------------------------------------------------------------------
#* La clase Director orquesta la construcción del objeto indicando 
#* el orden en que deben llamarse sus componentes, los mismos son
#* genéricos y dependerán del builder específico utilizado sus
#* valores concretos
#*--------------------------------------------------------------------
class Director:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
	   
   def getAvion(self):
      avion = Avion()
      
      # Primero el chasis
      body = self.__builder.getBody()
      avion.setBody(body)
      
      # Las 2 turbinas
      i = 0
      while i < 2:
        turbina = self.__builder.getTurbinas()
        avion.attach_turbinas(turbina)
        i += 1

      # Las 2 alas
      i = 0
      while i < 2:
        ala = self.__builder.getAlas()
        avion.attach_alas(ala)
        i += 1

      # Tren de aterrizaje
      tren_aterrizaje = self.__builder.getTrenDeaterrizaje()
      avion.setTrenDeaterrizaje(tren_aterrizaje)     

      # Retorna el avion completo
      return avion

#*----------------------------------------------------------------
#* Esta es la definición de un objeto avion inicializando 
#* todos sus atributos
#*----------------------------------------------------------------
class Avion:
   def __init__(self):
      self.__turbina = list()
      self.__body = None
      self.__alas = list()
      self.__tren_de_aterrizaje = None

   def setBody(self, body):
      self.__body = body

   def attach_turbinas(self, turbina):
      self.__turbina.append(turbina)

   def attach_alas(self, ala):
      self.__alas.append(ala)

   def setTrenDeaterrizaje(self, tren_aterrizaje):
      self.__tren_de_aterrizaje = tren_aterrizaje

   def specification(self):
      print ("chasis: %s" % (self.__body.shape))
      print ("turbinas: %d" % (self.__turbina[0].cantidad))
      print ("alas: %d\'" % (self.__alas[0].cantidad))
      print ("tren de aterrizaje: %d\'" % (self.__tren_de_aterrizaje.cantidad))

#*-----------------------------------------------------------------
#* Builder
#* Clase genérica que solo define la interfaz de los métodos que el
#* Builder específico tiene que implementar
#*-----------------------------------------------------------------
class Builder:
	
   def getBody(self): pass
   def getTurbinas(self): pass
   def getAlas(self): pass
   def getTrenDeaterrizaje(self): pass

#*-----------------------------------------------------------------
#* Esta es la hoja de ruta para construir un Avion
#* Establece instancias para tomar alas, tren de aterrizaje, chasis y turbinas
#* estableciendo las partes específicas que (en un Avion) 
#* deben tener esas partes
#*-------------------------------------------------------
class AvionBuilder(Builder):
   def getBody(self):
      body = Body()
      body.shape = "Militar"
      return body
   
   def getTurbinas(self):
      turbina = Turbinas()
      turbina.cantidad = 2
      return turbina
   
   def getAlas(self):
      ala = Alas()
      ala.cantidad = 2
      return ala
   
   def getTrenDeaterrizaje(self):
      tren_aterrizaje = TrenDeAterrizaje()
      tren_aterrizaje.cantidad = 1
      return tren_aterrizaje
   
   

#*----------------------------------------------------------------
#* Define partes genéricas para un avion (sin inicializar)
#*----------------------------------------------------------------

class Body:
   shape = None

class Turbinas:
   cantidad = None

class Alas:
   cantidad = None

class TrenDeAterrizaje:
   cantidad = None

#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* Esta es la estructura main()
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def main():

#*----------------------------------------------------------------
#* Instancia la clase que será el resultado y la que guiará el 
#* proceso de construcción
#*----------------------------------------------------------------
   avionBuilder = AvionBuilder() # initializing the class
   director = Director()

#*----------------------------------------------------------------
#* Pasa al director la hoja de ruta para construir un Avion
#*----------------------------------------------------------------   
   director.setBuilder(avionBuilder)

#*----------------------------------------------------------------
#* Ordena al director agregar los componentes de un Avion según
#* la hoja de ruta
#*----------------------------------------------------------------
   avion = director.getAvion()

#*---------------------------------------------------------------
#* Finalizada la construcción verifica que sea completa
#*---------------------------------------------------------------
   avion.specification()
   print()

#*----------------------------------------------------------------------
#* Se detecta el entry point y se lo deriva a una sección main() propia
#*----------------------------------------------------------------------
if __name__ == "__main__":
   print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avion")
   print()
   main()
