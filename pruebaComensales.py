import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

semaPlato = threading.Semaphore(1)
semaCoci = threading.Semaphore(0)

platosDisponibles = 3

class Cocinero(threading.Thread):
  def __init__(self):
    super().__init__()
    self.name = 'Cocinero'

  def run(self):
    global platosDisponibles

    while (True):
      semaCoci.acquire()
      try:
        logging.info('Reponiendo los platos...')
        platosDisponibles = 3
      finally:
        semaPlato.release() # con este le hace release al thread q le sigue al cuarto x ejemplo q come y le hace release al tercero

class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
    global platosDisponibles
    
    semaPlato.acquire()
    try:
      #while platosDisponibles == 0:
      if platosDisponibles == 0:  #el intento fallido en clase.
        semaCoci.release()
        semaPlato.acquire() # viene el tercer thread y se frena aca hasta q el cuarto come y hace release
      self.comer()
    finally:
        semaPlato.release()

  def comer(self):
    global platosDisponibles
    platosDisponibles -= 1
    logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')



Cocinero().start()

for i in range(178):
  Comensal(i).start()