import pickle
x=2
f = open("data/questions.dat","ab")
while x>1:
    x = input("Enter the question:")
    y = input("Enter the answer:")
    L = [x,y]
    pickle.dump(L,f)
    u = input("Do you want to terminate the code?:")
    if u in ("Yes", "yes"):
        break
    else:
        x = 2
f.close()