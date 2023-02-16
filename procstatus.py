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