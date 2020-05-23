import time
def check_password(password): # Don't change it
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1) # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True

def crack_password():
    tpass = [0,0,0,0]
    start = 0
    end = 0.1
    for i in range(4):
        while (end-start)<(0.1*(i+2)):
            start = time.time()
            result = check_password(tpass)
            end = time.time()
            if result == True:
                return tpass
            tpass[i] = tpass[i] + 1
        tpass[i] = tpass[i] - 1

inp = input('A real password: ')
real_password = [int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3])]
pas = crack_password()
print(pas)
