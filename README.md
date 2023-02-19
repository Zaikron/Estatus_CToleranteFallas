> # UDG - CUCEI 
> #### 20 de febrero de 2023
### <p align="left"> Anthony Esteven Sandoval Marquez, 215660767</p>
### <p align="center"> Materia: Computacion Tolerante a Fallas </p>
### <p align="center"> Profesor: Michel Emanuel López Franco </p>
### <p align="center"> Ciclo: 2023-A </p>

> ## Estatus

#### Este programa recibe como parámetros nombres de programas para detectar su estado de ejecución. Se hacen las pruebas con el programa que realizamos en la actividad anterior, en mi caso el mío se llama Checkpoint.exe, por lo tanto pasare ese parámetro al script de Python. Para ver el estatus se muestra un texto que indica tal situación, el color rojo indica que el proceso no existe y en verde que el proceso se está ejecutando.
<p align="center"> <img src="https://github.com/Zaikron/Estatus_CToleranteFallas/blob/main/Estatus_Im/c1.gif"/> </p>

#### Creación del servicio
<p align="center"> <img src="https://github.com/Zaikron/Estatus_CToleranteFallas/blob/main/Estatus_Im/c2.PNG"/> </p>

#### Ejecución del servicio
<p align="center"> <img src="https://github.com/Zaikron/Estatus_CToleranteFallas/blob/main/Estatus_Im/c3.PNG"/> </p>
<p align="center"> <img src="https://github.com/Zaikron/Estatus_CToleranteFallas/blob/main/Estatus_Im/c4.PNG"/> </p>


```python
  import sys
  import psutil
  from sys import stdout
  import time

  def check_arguments():
      if len(sys.argv) == 1:
        print('Este programa no funciona sin argumentos')
        sys.exit(0)

  def get_targets():

      targets = sys.argv[1:]

      i = 0
      while i < len(targets):

        if not targets[i].endswith('.exe'):
          targets[i] = targets[i] + '.exe'

        i += 1

      return targets

  def getChar(num):
      if(num == 0):
          return '|'
      if(num == 1):
          return '/'
      if(num == 2):
          return '—'
      if(num == 3):
          return '\\'


  def lock(target):
      num = 0
      for proc in psutil.process_iter():
          if proc.name().lower() == target.lower():
              stdout.write("\r \033[4;42m El proceso %s Se esta ejecutando %s" % (proc.name(), getChar(num)))
              stdout.flush()
              time.sleep(1)
          else:
              stdout.write("\r \033[4;41m El proceso %s No se esta ejecutando %s" % (target, getChar(num)))
              stdout.flush()

          num += 1
          if(num > 3):
              num = 0

  if __name__ == '__main__':

      check_arguments()
      targets = get_targets()

      while True:
        for target in targets:
            lock(target)
```
