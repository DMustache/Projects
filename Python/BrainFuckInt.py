def main():
    fifi=100
    arr=[]
    m1=0
    for i in range (100,1000):
        arr.append(str(i))
        m1+=1
    print(m1)
    print(arr)
    m=0
    for fifi in arr:


        if (fifi[0]==fifi[1] or fifi[0]==fifi[2] or fifi[1]==fifi[2]) and not(fifi[0]==fifi[1]==fifi[2]) :
            m+=1
            print(fifi)

    print(m/m1)
if __name__ == '__main__':
    main()