
from initdata import bob, sue
import shelve

db = shelve.open('people_shelve')
db['bob'] = bob
db['sue'] = sue

db.close()
print(db)
