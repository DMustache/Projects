from pushbullet import PushBullet
from datetime import datetime

time = datetime.now()
time = time.strftime('%m/%d/%Y %H:%M:%S')

string = f'Выполнен вход в аккаунт в {time}'

pb = PushBullet(api_key='o.3tArpZZZoGmofAMKHzQ7TdAaS2DaEpbp')

phone = pb.devices[0]

push = pb.push_note('Зафиксирован вход', string)

f = open(r'C:\Users\Dmitry\Documents\Projects\Python\keylogger\file.log', mode='a', encoding='utf-8')
f.write(string + '\n')
f.close()