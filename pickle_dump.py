import pickle
st = ['hii','hoe','are',10]
with open('nnb_pickle.info','wb') as fp:
    pickle.dump(st,fp)
print('is file colosed',fp.closed)

