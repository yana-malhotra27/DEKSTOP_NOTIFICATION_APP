import pickle
f = open("data/questions1.dat","rb")
try:
    while True:
        L = pickle.load(f)
        print(L)
except EOFError:
    f.close()