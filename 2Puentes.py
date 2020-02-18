import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20
semaforoPuente1=threading.Semaphore(1)
semaforoPuente2=threading.Semaphore(1)

class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.5)

  def avanzar(self):
    time.sleep(self.velocidad)
    self.posicion += 1

  def dibujar(self):
    print(' ' * self.posicion + "🐮")

  def run(self):
    while(True):
      if self.posicion==9:
        semaforoPuente1.acquire()
      if self.posicion==39:
        semaforoPuente2.acquire()
      try:
        self.avanzar()
      finally:
        if self.posicion==31:
            semaforoPuente1.release()
        if self.posicion==101:
            semaforoPuente2.release()
        


vacas = []
for i in range(5):
  v = Vaca()
  vacas.append(v)
  v.start()

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def dibujarPuente():
  print(' ' * inicioPuente + '=' * largoPuente + ' ' * inicioPuente + '=' * largoPuente*3)

while(True):
  cls()
  print('Apretá Ctrl + C varias veces para salir...')
  print()
  dibujarPuente()
  for v in vacas:
    v.dibujar()
  dibujarPuente()
  time.sleep(0.2)
