
bob = {
    'name': {
        'last': 'Bob',
        'first': 'Smith'
    },
    'age': 20,
    'job': ['software', 'writing']
}
sue = {'name': 'sue', 'age': 20, 'pay': 30, 'job': 'student'}
tom = {'name': 'tom', 'age': 50, 'pay': 0, 'job': None}

db = dict()
db['sue'] = sue
db['bob'] = bob
db['tom'] = tom

if __name__ == '__main__':
    for key in db:
        print(key, '==>\n', db[key])
