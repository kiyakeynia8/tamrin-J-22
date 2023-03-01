import sqlite3

class Database():
    def __init__(self):
        self.con = sqlite3.connect("todo_list.db")
        self.cursor = self.con.cursor()
        self.tasks = []

    def get_tasks(self):
        query = "SELECT * FROM tasks"
        result = self.cursor.execute("SELECT * FROM tasks")
        self.tasks = result.fetchall()
        return self.tasks

    def add_new_task(self,new_title,new_description):
        try:
            query = f"INSERT INTO tasks(title, description)VALUES('{new_title}', '{new_description}')"
            self.cursor.execute(query)
            self.con.commit()
            return True
        
        except:
            return False

    def remove_task(self,id):
        self.cursor.execute(f"DELETE FROM tasks WHERE id = '{id}'")
        self.con.commit()
    
    def task_done(self,id):
        self.cursor.execute(f'SELECT * FROM tasks WHERE id = "{id}"')
        task = self.cursor.fetchall()
        if task != None:
            new_id = len(self.tasks) + 1
            self.cursor.execute(f'UPDATE tasks SET is_done = 1 WHERE id = {id}')
            self.cursor.execute(f'UPDATE tasks SET id = {new_id} WHERE is_done = 1')
            self.con.commit()