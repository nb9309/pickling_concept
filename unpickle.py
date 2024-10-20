import pickle

with open('nnb_pickle.info','rb') as fp:
    rp = pickle.load(fp)
    print(rp)
print('is file colosed',fp.closed)