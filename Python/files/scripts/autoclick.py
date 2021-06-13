import os

def onWork():
    os.system("netsh inteface set inteface 'Работать' enabled")

def onDownload():
    os.system('netsh interface set interface Скачать enabled')

onWork()