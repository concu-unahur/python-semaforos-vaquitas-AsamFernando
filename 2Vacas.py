import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20

semaforoInicioPuente=threading.Semaphore(2)
#semaforoFinPuente=threading.Semaphore(0)
vacasCruzaron=0
cantVacas=8

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
    global vacasCruzaron
    while(True):
      self.avanzar()
      try:
        if self.posicion==inicioPuente - 1:
          semaforoInicioPuente.acquire()
        elif self.posicion==inicioPuente + largoPuente + 1:
          vacasCruzaron+=1
      finally:
        if vacasCruzaron==2:
          vacasCruzaron=0
          for i in range(2):
            semaforoInicioPuente.release()

          
vacas = []
for i in range(cantVacas):
  v = Vaca()
  vacas.append(v)
  v.start()

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def dibujarPuente():
  print(' ' * inicioPuente + '=' * largoPuente)

while(True):
  cls()
  print('Apretá Ctrl + C varias veces para salir...')
  print()
  dibujarPuente()
  for v in vacas:
    v.dibujar()
  dibujarPuente()
  time.sleep(0.2)
