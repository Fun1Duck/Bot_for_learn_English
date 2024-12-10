import sqlite3


class Users_dicts:
    name_db = 'users_dicts.db'

    def __init__(cls, user_id):
        cls.user_id = 'table_' + str(user_id)
        with sqlite3.connect(cls.name_db) as db:
            c = db.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS {} (
                                        words TEXT
                                        )""".format(cls.user_id))
            db.commit()

    @classmethod
    def add_word(cls, user_id, word):
        with sqlite3.connect(cls.name_db) as db:
            c = db.cursor()
            c.execute(f"SELECT words FROM {user_id} WHERE rowid = 1")
            result = c.fetchone()
            if result:
                result = tuple(result[0].rstrip().split('\n'))
                if len(result) == 150:
                    c.execute(
                        f"UPDATE {user_id} SET words = ? WHERE rowid = 1",
                        ('\n'.join(result[1:]) + '\n',))
            c.execute(
                f"INSERT OR REPLACE INTO {user_id} (rowid, words) VALUES ((SELECT rowid FROM {user_id} LIMIT 1), COALESCE((SELECT words FROM {user_id}), '') || ?)",
                (word + '\n',))
            db.commit()


    @classmethod
    def get_words(cls, user_id):
        with sqlite3.connect(cls.name_db) as db:
            c = db.cursor()
            c.execute(f"SELECT words FROM {user_id} WHERE rowid = 1")
            result = c.fetchone()
            db.commit()
        if result:
            return result[0].rstrip()
        return


class Users_words:
    name_db = 'users_words.db'

    def __init__(cls, user_id):
        cls.user_id = 'table_' + str(user_id)
        with sqlite3.connect(cls.name_db) as db:
            c = db.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS {} (
                                        info varchar(100),
                                        timer INTEGER
                                        )""".format(cls.user_id))
            db.commit()


    @classmethod
    def add_user_info(cls, user_id, info, timer):
        with sqlite3.connect(cls.name_db) as db:
            c = db.cursor()
            c.execute(
                f"INSERT INTO {user_id} (info, timer) VALUES (?, ?)",
                (info, timer))
            db.commit()


    @classmethod
    def update_words(cls, user_id, info_old, info, timer):
        with sqlite3.connect(cls.name_db) as db:
            c = db.cursor()
            c.execute(
                f"UPDATE {user_id} SET info = ?, timer = ? WHERE info = ?",
                (info, timer, info_old))
            db.commit()


    @classmethod
    def get_info(cls, user_id, timer):
        with sqlite3.connect(cls.name_db) as db:
            c = db.cursor()
            c.execute(f"SELECT info FROM {user_id} WHERE timer = ? LIMIT 1",
                      (timer,))
            result = c.fetchone()[0]
            db.commit()
        return result


    @classmethod
    def delete_info(cls, user_id, info, timer):
        with sqlite3.connect(cls.name_db) as db:
            c = db.cursor()
            c.execute(
                f"DELETE FROM {user_id} WHERE info = ? AND timer = ?",
                (info, timer))
            db.commit()


class Users:
    name_db = 'users_bot_learn_language.db'

    def __init__(self, name):
        self.name = name
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS {} (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        user_id INTEGER,
                                        native_lang varchar(15),
                                        will_learn_lang varchar(15),
                                        level varchar(2),
                                        theme TEXT,
                                        quantity_words INTEGER
                                        )""".format(self.name))
            db.commit()


    def add_user_info(self, id, data: dict):
        native_lang, will_learn_lang, level, quantity_words = data.values()
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(
                f"INSERT INTO {self.name} (user_id, native_lang, will_learn_lang, level, quantity_words) VALUES (?, ?, ?, ?, ?)",
                (id, native_lang, will_learn_lang, level, quantity_words))
            db.commit()


    def get_level(self, id):
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(f"SELECT level FROM {self.name} WHERE user_id = ?",
                      (id,))
            result = c.fetchone()[0]
            db.commit()
        return result

    def get_users_ids(self):
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(f"SELECT user_id FROM {self.name}")
            result = c.fetchone()
            db.commit()
        if not result:
            return  tuple()
        return result
    
    def get_quantity_words(self, id):
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(f"SELECT quantity_words FROM {self.name} WHERE user_id = ?",
                      (id,))
            result = c.fetchone()[0]
            db.commit()
        return result


    def increase_level(self, id):
        data = {'A1': 'A2', 'A2': 'B1', 'B1': 'B2', 'B2': 'C1', 'C1': 'C2', }
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(f"SELECT level FROM {self.name} WHERE user_id = ?",
                      (id,))
            result = c.fetchone()[0]
            if result in ('C1',):
                return
            new_level = data[result]
            c.execute(
                f"UPDATE {self.name} SET level = ? WHERE user_id = ?",
                (new_level, id))
            db.commit()


    def reduce_level(self, id):
        data = {'A2': 'A1', 'B1': 'A2', 'B2': 'B1', 'C1': 'B2', 'C2': 'C1', }
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(f"SELECT level FROM {self.name} WHERE user_id = ?",
                      (id,))
            result = c.fetchone()[0]
            if result in ('A1',):
                return
            new_level = data[result]
            c.execute(
                f"UPDATE {self.name} SET level = ? WHERE user_id = ?",
                (new_level, id))
            db.commit()


    def get_learn_lang(self, id):
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(f"SELECT will_learn_lang FROM {self.name} WHERE user_id = ?",
                      (id,))
            result = c.fetchone()[0]
            db.commit()
        return result

    def new_quantity_words(self, id, num):
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(
                f"UPDATE {self.name} SET quantity_words = ? WHERE user_id = ?",
                (num, id))
            db.commit()


    def update_theme(self, id, theme):
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(
                f"UPDATE {self.name} SET theme = ? WHERE user_id = ?",
                (theme, id))
            db.commit()


class DataBase_words_language:
    name_db = 'words.db'

    def __init__(self, name):
        self.name = name
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS {} (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        level varchar(2),
                                        words TEXT
                                        )""".format(self.name))
            if self.name == 'usa':
                for level in ('A1','A2', 'B1', '5000', 'B2', 'C1', 'agro'):
                    c.execute(f"SELECT COUNT(*) FROM {self.name} WHERE level = ?", (level,))
                    result = c.fetchone()[0]
                    if result == 0:
                        with open(f'usa_{level}.txt', encoding='utf-8') as f:
                            words = f.read()
                            c.execute(
                                f"INSERT INTO {self.name} (level, words) VALUES (?, ?)",
                                (level, words))
            if self.name == 'rus':
                for level in ('A1','A2', 'B1', 'B2', 'C1'):
                    c.execute(f"SELECT COUNT(*) FROM {self.name} WHERE level = ?", (level,))
                    result = c.fetchone()[0]
                    if result == 0:
                        with open(f'rus_{level}.txt', encoding='utf-8') as f:
                            words = f.read()
                            c.execute(
                                f"INSERT INTO {self.name} (level, words) VALUES (?, ?)",
                                (level, words))
            db.commit()


    def get_words_level(self, level):
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(f"SELECT words FROM {self.name} WHERE level = ?",
                      (level,))
            result = c.fetchone()[0]
            db.commit()
        return result


class User_study_words:
    name_db = 'users_bot_learn_language.db'

    def __init__(self, name):
        self.name = name
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS {} (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        user_id INTEGER,
                                        words_study_level TEXT,
                                        learning_words TEXT,
                                        in_process TEXT,
                                        learnt_words TEXT
                                        )""".format(self.name))
            db.commit()


    def add_words_study_level(self, id, words):
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(
                f"INSERT INTO {self.name} (user_id, words_study_level) VALUES (?, ?)",
                (id, words))
            db.commit()


    def update_words_study_level(self, id, words):
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(
                f"UPDATE {self.name} SET words_study_level = ? WHERE user_id = ?",
                (words, id))
            c.execute(
                f"UPDATE {self.name} SET learning_words = NULL WHERE user_id = ?",
                (id,))
            db.commit()


    def get_percent_of_level(self, id):
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(f"SELECT learnt_words, words_study_level FROM {self.name} WHERE user_id = ?",
                      (id,))
            res = c.fetchall()[0]
            learnt_words, words_study_level = res
            db.commit()
        if learnt_words is None:
            return 0
        return round(100 - round(len(list(set(words_study_level.split('\n')) - set(learnt_words.split('\n')))) / len(words_study_level.split('\n')) * 100, 2), 2)

    def get_words(self, id):
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(f"SELECT words_study_level FROM {self.name} WHERE user_id = ?",
                      (id,))
            res = c.fetchone()[0]
            c.execute(f"SELECT learnt_words FROM {self.name} WHERE user_id = ?",
                      (id,))
            res1 = c.fetchone()[0]
            c.execute(f"SELECT in_process FROM {self.name} WHERE user_id = ?",
                      (id,))
            res2 = c.fetchone()[0]
            db.commit()
        if not res1 and not res2:
            return tuple(res.split('\n'))
        elif not res2:
            return tuple(set(res.split('\n')) - set(res1.split('\n')))
        elif not res1:
            return   tuple(set(res.split('\n')) - set(res2.split('\n')))
        return  tuple(set(res.split('\n')) - set(res1.split('\n')) - set(res2.split('\n')))

    def add_learnt_word(self, id, word):
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(
                f"UPDATE {self.name} SET learnt_words = COALESCE(learnt_words, '') || ? WHERE user_id = ?",
                (word + '\n', id))
            db.commit()


    def get_len_learning_words(self, id):
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(f"SELECT learning_words FROM {self.name} WHERE user_id = ?",
                      (id,))
            res = c.fetchone()[0]
            db.commit()
        if res is None:
            return 0
        return len(res.split('\n')[:-1])

    def add_learning_word(self, id, word):
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(
                f"UPDATE {self.name} SET learning_words = COALESCE(learning_words, '') || ? WHERE user_id = ?",
                (word + '\n', id))
            db.commit()


    def add_word_in_process(self, id, word):
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(
                f"UPDATE {self.name} SET in_process = COALESCE(in_process, '') || ? WHERE user_id = ?",
                (word + '\n', id))
            db.commit()


    def delete_learning_words(self, id):
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(
                f"UPDATE {self.name} SET learning_words = NULL WHERE user_id = ?",
                (id,))
            db.commit()


    def delete_words_in_process(self, id, l):
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(f"SELECT in_process FROM {self.name} WHERE user_id = ?",
                      (id,))
            res = c.fetchone()[0].split('\n')
            res1 = '\n'.join(res[5:])
            c.execute(
                f"UPDATE {self.name} SET in_process = ? WHERE user_id = ?",
                (res1, id))
            c.execute(
                f"UPDATE {self.name} SET learnt_words = COALESCE(learnt_words, '') || ? WHERE user_id = ?",
                (res1, id))
            db.commit()


    def get_learning_words(self, id):
        with sqlite3.connect(self.name_db) as db:
            c = db.cursor()
            c.execute(f"SELECT learning_words FROM {self.name} WHERE user_id = ?",
                      (id,))
            res = c.fetchone()[0]
            db.commit()
        return res.split('\n')[:-1]