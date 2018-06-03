import random, time
a = 0
b = 0
c = 0

default_a = 1
default_b = 5
default_c = 1.2
seikai = 0
kaisu = 1

while True:
    kekka = 0
    keta = 0
    x = 0
    goukei = 0
    keta = 0
    keisan = 0
    kotae = 0
    n = 0
    seikai = 0
    kaisu = 1
    s = 0
    a = 1
    b = 5
    c = 1.2
    mx = 15
    d = 0
    a = input("Input digit: ")
    if a == '':
        a = default_a
        print ("digit => ") 
        print(a)
    if a == 1:
        print("Cool.")
    if a == 2:
        print('Wow, you must be cool')

    b = input("repetition?: ")
    if b == '':
        b = default_b
        print (b)
        print ("times")
    if b <= mx:
        default_b = b


    c = input("speed?: ")
    if c == '':
        c = default_c
    if c <= 2.0:   
        print("Hussle!")
        c = default_c
        print("Set to "+str(c) + "sec. Go for it!")
    time.sleep(2)
    n = a
    d = pow(10,n)-1
    #d = d- 1
    #print(n) for debugging
    #print(d)
    for foo in range(b):
        keta = random.randint(1,d)
        print(keta)
        time.sleep(c)
        goukei = goukei + keta

    kotae = int(input("The answer is...\n"))
    time.sleep(2.0)
    print(goukei)
    if kotae == goukei:
        print("You got it!")
        seikai += 1
        kaisu += 1
        print (seikai)
    if seikai == 0:
        print ("seikai nashi, so far")
    else:
        print (str(float(seikai) / float(kaisu)) + "%")
    answer = input('Try again? (y/n): ')
    if answer in ('y', 'n'):
        #break
    #print 'Invalid input.'
        if answer == ('y' or ''):
            continue
        else:
            print ('Goodbye')
            break
