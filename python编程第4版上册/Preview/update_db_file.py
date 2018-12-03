from use_script import loadDbase, storeDbase

db = loadDbase()
db['sue']['pay'] = 40
db['tom']['name'] = 'Tom Tom'
storeDbase(db)
