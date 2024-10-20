import pickle
with open('pw.word', 'ab') as fp:
    lst = [30,45,67,'hari']
    pickle.dump(lst,fp)
print('is file closed: ',fp.closed)