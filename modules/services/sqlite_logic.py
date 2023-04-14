import sqlite3

def dict_factory(cursor, row):
    save_dict = {}
    for idx, col in enumerate(cursor.description):
        save_dict[col[0]] = row[idx]
    return save_dict

def update_format_args(sql, parameters: dict):
    sql = f"{sql} WHERE "
    sql += " AND ".join([
        f"{item} = ?" for item in parameters
    ])
    return sql, list(parameters.values())

def update_format(sql, parameters: dict):
    if "XXX" not in sql: sql += " XXX "

    values = ", ".join([
        f"{item} = ?" for item in parameters
    ])
    sql = sql.replace("XXX", values)

    return sql, list(parameters.values())


class DataBase:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file,  check_same_thread=False)
        self.cur = self.connection.cursor()

    def start_bot(self, colorama):
        #БД с пользователями
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS
        files(
        file_name TEXT PRIMARY KEY,
        attachemnt_id TEXT)""")

        self.connection.commit()
        print(colorama.Fore.RED + "--- Базы данных подключены ---")


    def add_file(self, file_name, attachemnt_id):
        data = self.cur.execute("SELECT file_name FROM files  WHERE file_name = ?", (file_name,)).fetchone()
        if data == None:
            self.cur.execute("INSERT INTO files (file_name, attachemnt_id) VALUES (?, ?)",[file_name,  attachemnt_id])
            self.connection.commit()
            return True
        else:
            return False



