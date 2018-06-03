import random, time
while True:
    a = 0
    b = 0
    c = 0
    seikai = 1
    kaisu = 1
    def setup(digit=1, freq=5, speed=1.2):
       return(a,b,c)
    a = (raw_input("Input digit: "))
    if a == 1:
        print("Cool.")
    elif a == 2:
        print('Wow, you musst be cool')
    elif a == '':
        a = 1
    print ("digit = " + str(a))
    b = (raw_input("repetition?: "))
    if b <= 15:
        
        print str(b)+" times"
    elif b == '':
        b = 5
        print ("5 times")
    c = (raw_input("speed?: "))
    if c < 2.0:   
        print("Hussle!")
        
    elif c == '':
        c = 1.2
        print(str(c)+"sec. Go for it!")
    time.sleep(2)

    kekka = 0
    keta = 0
    d = 0
    goukei = 0
    keta = 0
    keisan = 0
    kotae = 0
    kaisu += 1
    n = a
    d = 10 ** n - 1
    for foo in range(b):
        keta = random.randint(1,d)
        print(keta)
        time.sleep(c)
        goukei = goukei + keta

    kotae = (input("The answer is...\n"))
    time.sleep(2.0)
    print(goukei)
    if kotae == goukei:
        print('You got it!')
        seikai += 1
    if seikai == 0:
        print ("seikai nashi, so far")
    else:
        print str(float(seikai)* 100 / float(kaisu)) + "%"
    answer = raw_input('Try again? (y/n): ')
    if answer in ('y', 'n'):
        #break
    #print 'Invalid input.'
        if answer == ('y',''):
            continue
        else:
            print 'Goodbye'
            break