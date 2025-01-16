import pickle
f = open("data/questions.dat","rb")
try:
    while True:
        L = pickle.load(f)
        print(L)
except EOFError:
    f.close()