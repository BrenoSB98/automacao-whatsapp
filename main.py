# Passo a Passo do projeto
# Passo 1 - Entrar no whatsapp
# importar as bibliotecas
import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 1

# abrir navegador
pyautogui.press('win')
pyautogui.write('whatsapp')
pyautogui.press('enter')
time.sleep(3)

# Passo 2 - Procurar o contato "Amor"
pyautogui.click(x=211, y=123)
pyautogui.write('Amor')
pyautogui.click(x=212, y=193)

# Passo 3 - Escrever e Enviar a mensagem
pyautogui.click(x=573, y=1013)
pyautogui.write('Bom diaaaa meu amor!!')
pyautogui.press('enter')
pyautogui.write('Estou feliz em acordar mais um dia e saber que eu tenho a mulher mais linda e incrivel desse mundo ao meu lado.')
pyautogui.press('enter')
pyautogui.write('Te amo muito, tenha um otimo dia.')
pyautogui.press('enter')
# Passo 4 - Fecha o Whatsapp
pyautogui.click(x=1900, y=16)
