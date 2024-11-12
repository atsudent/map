import pyautogui
import time
import keyboard
 
def cautare_google():
    if pyautogui.locateOnScreen(r"E:\UB\python\lab1\bot\image.png", confidence=0.2) != None:
        # print("Bara de cautare a fost gasita")
        bara_cautare = pyautogui.locateOnScreen(r"E:\UB\python\lab1\bot\image.png", confidence=0.2)
        pyautogui.click(bara_cautare)
        time.sleep(1)
        pyautogui.write("https://www.youtube.com/watch?v=1R47EQrxgfw")
        pyautogui.press('enter')
 
def click_videoclipuri():
    time.sleep(3)
    pyautogui.click(1793, 544)
 
def afisare_coordonate():
    while not keyboard.is_pressed('x'):
        print(pyautogui.position())
        time.sleep(0.2)
 
raspuns = pyautogui.confirm("Vrei sa incepi rularea programului?", "Confirmare")
if raspuns == "OK":
    cautare_google()
    click_videoclipuri()
else:
    afisare_coordonate()