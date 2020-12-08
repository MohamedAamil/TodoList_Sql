import sqlite3

def insert_into_table(task,pri):
    sql_insert_query = """
    INSERT INTO tasks(TaskName, Complete,Priority) VALUES ('%s', %s , '%s')
    """ %(task,0,pri)

    execute_query(sql_insert_query)

def select_all_records(comp):
    if comp == "0":
        sql_select_query = """SELECT Taskname FROM tasks WHERE complete = 0 ORDER BY Priority"""
        result = execute_query(sql_select_query).fetchall()
        return [x[0] for x in result]
    else:
        sql_select_query = """SELECT Taskname FROM tasks WHERE complete = 1 ORDER BY Priority"""
        result = execute_query(sql_select_query).fetchall()
        return [x[0] for x in result]

def execute_query(sql):
    with sqlite3.connect("Data") as conn:
        cur = conn.cursor()
        result = cur.execute(sql)
        conn.commit()
    return result

def mark_as_complete(task):
    sql = """
    UPDATE tasks
    SET Complete = 1
    WHERE Taskname = '%s' AND Complete = 0
    """%(task)

    execute_query(sql)

def change_task(task,chag,pri):
    sql = """
    UPDATE tasks
    SET Taskname = '%s' , Priority = '%s'
    WHERE Taskname = '%s'
    """%(chag,pri,task)

    res = execute_query(sql).fetchall()



if __name__ == "__main__":
    select_all_records()
