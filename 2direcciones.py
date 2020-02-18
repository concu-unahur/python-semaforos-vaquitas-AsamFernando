import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20
semaforoPuente1=threading.Semaphore(1)
semaforoPuente2=threading.Semaphore(1)


class Puente:
  def __init__(self, inicioPuente, largoPuente):
    self.inicio=inicioPuente
    self.largo=largoPuente

  def dibujoPuente(self):
    return ' ' * self.inicio + '=' * self.largo
  
  def distanciaAbarca(self):
    return self.inicio + self.largo

listaPuentes=[Puente(10, 20)]#, Puente(10, 40)]


def inicioDelPuente(nroPuente):
  total=listaPuentes[nroPuente].distanciaAbarca()
  for i in range(nroPuente):
    total+=listaPuentes[i].distanciaAbarca()
  return total - listaPuentes[nroPuente].largo - 1


class Vaca(threading.Thread):

    def __init__(self, posicion, avanza):
      super().__init__()
      self.posicion = posicion
      self.velocidad = random.uniform(0.1, 0.5)
      self.avanza = avanza

    def avanzar(self):
      time.sleep(self.velocidad)
      self.posicion += 1
    
    def retroceder(self):
      time.sleep(self.velocidad)
      self.posicion-=1

    def dibujar(self):
      print(' ' * self.posicion + "🐮")


    def run(self):
      while(True):
        if self.posicion==9 and self.avanza:
            semaforoPuente1.acquire()
        if self.posicion==31 and not self.avanza:
            semaforoPuente1.acquire()
        try:
          if self.avanza:
              self.avanzar()
          else:
              self.retroceder()
        finally:
          if self.posicion==31 and self.avanza:
              semaforoPuente1.release()
          if self.posicion==9 and not self.avanza:
              semaforoPuente1.release()
        
        
posiciones=[0, 40, 0, 40, 0]
vacas = []
for posicion in posiciones:
  v = Vaca(posicion, posicion==0)
  vacas.append(v)
  v.start()

def cls():
  os.system('cls' if os.name=='nt' else 'clear')


def dibujarPuente():
  todosLosPuentes=''
  for puente in listaPuentes:
    todosLosPuentes+=puente.dibujoPuente()
  print(todosLosPuentes)

while(True):
  cls()
  print('Apretá Ctrl + C varias veces para salir...')
  print()
  dibujarPuente()
  for v in vacas:
    v.dibujar()
  dibujarPuente()
  time.sleep(0.2)
