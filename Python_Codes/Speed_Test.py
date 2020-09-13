#Made by: Vinícius Azevedo
#Instagram: instagram.com/v.mazevedo
#Twitter: twitter.com/vmeazevedo

import speedtest   
from hurry.filesize import size, si
import time
  
st = speedtest.Speedtest()

print('Iniciando o teste de velocidade.')
print('Aguarde...')
time.sleep(2)

print()
print('Resultado:')
#Download
print('\n===DOWNLOAD===')
down = st.download() 
print(down, 'bits/s')   
print('Resultado:',size(down))

#Upload
print('\n===UPLOAD===')
up = st.upload()
print(up, 'bits/s')   
print('Resultado:',size(up))

#Ping
print('\n===PING===')
servernames =[]   
st.get_servers(servernames)   
print('Resultado:',st.results.ping)   

wait = input('\nPressione qualquer tecla para finalizar...')