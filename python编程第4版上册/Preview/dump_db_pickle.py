import pickle

with open('people_pickle', 'rb') as dbfile:
    db = pickle.load(dbfile)

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tome Tom'

with open('people_pickle', 'wb') as dbfile:
    pickle.dump(db, dbfile)
    print(db)
