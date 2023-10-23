import os
import sys

print('\033[2;32;43m Installing python packages...')	

os.system('cmd /c "pip install colorsys"')
os.system('cmd /c "pip install math"')
os.system('cmd /c "pip install random"')
os.system('cmd /c "pip install pygame"')
os.system('cmd /c "pip install librosa"')
os.system('cmd /c "pip install librosa.display"')
os.system('cmd /c "pip install matplotlib.pyplot"')
os.system('cmd /c "pip install numoy"')
os.system('cmd /c "pip install time"')
os.system('cmd /c "pip install ctypes"')

dirname = os.path.dirname("Server")
file_path = 'c:/users/' + os.getlogin()
filename = os.path.join(dirname, file_path,'./Documents/My Bedrock Server/MCBE Server/Server' )

os.mkdir(filename)

# mode
mode = 0o666
  
# Path
path = os.path.join(filename)
  
print("Directory '% s' created" )

sys.exit()