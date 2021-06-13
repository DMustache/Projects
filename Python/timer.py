import time, sys, os

select = str(input())
while True:
    os.system('cls')
    if select == '1':
        localTime = time.ctime()
        print(localTime)
    elif select == '2':
        time.sleep(float(input()) * 60)
        print('STOP')

    elif select == '/exit':
        sys.exit()
    else:
        print('--???--')
    select = str(input())
