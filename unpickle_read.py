import pickle
with open('pw.word','rb') as fp:
    rp = pickle.load(fp)
    print(rp)
print('is file closed',fp.closed)