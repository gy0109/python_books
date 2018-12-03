
dbfilename = 'people-file'
ENDDB = 'enddb'
ENDREC = 'endrec'
RECSEP = '==>'


def storeDbase(db, dbfilename=dbfilename):
    # 将数据库格式化保存为普通文件
    # db_file = open(dbfilename,  encoding='utf-8')
    with open(dbfilename, 'w', encoding='utf-8') as db_file:
        for key in db:
            print(key, file=db_file)
            for (name, value) in db[key].items():
                print(name + RECSEP + repr(value), file=db_file)
            print(ENDREC, file=db_file)
        print(ENDDB, file=db_file)


def loadDbase(dbfilename=dbfilename):
    # 解析数据,重新构建数据库
    with open(dbfilename, encoding='utf-8') as db_file:
        import sys
        sys.stdin = db_file
        db = {}
        key = input()
        while key != ENDDB:
            rec = {}
            field = input()
            while field != ENDREC:
                name, *value = field.split(RECSEP)
                print(name, *value)
                rec[name] = eval(*value)
                field = input()

            db[key] = rec
            key = input()
    return db


if __name__ == '__main__':
    from initdata import db
    storeDbase(db)
