
import shelve
db = shelve.open('people_class_shelve')
for key in db:
    print(key, '==>', db[key].name, db[key].pay)
bob = db['bob']
print(db['bob']['name'])
print(bob.lasename)
db.close()
