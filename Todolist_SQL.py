import PySimpleGUI as sg
from DataBase_Operation import insert_into_table,select_all_records,mark_as_complete,change_task,change_task

sg.theme("Material2")

task = select_all_records("0")

layout = [
    [sg.Image("Title.png", size = (610, 100))],
    [sg.Text("To Do: " , font = ("Simplified Arabic Fixed",15), pad = (20,20)),
     sg.InputText("" , size = (35 , 1), font = ("Simplified Arabic" , 14), key = 'task' , background_color= "white" , text_color= "black" ),
     sg.Combo([ 'High' , 'Low' , 'Very Low'] ,font = ("Simplified Arabic Fixed" , 9) , background_color= "white", text_color= "black" , key = 'priority' , default_value = 'Low' ) ],
    [sg.Button("Completed" , font = ("Simplified Arabic Fixed" , 10) , pad = (140 , 10), key = 'comp'),sg.Button("Incomplete" , font = ("Simplified Arabic Fixed" , 10) , key = 'incomp') ],
    [sg.Button("Add", font = ("Simplified Arabic Fixed", 15) , key = 'add_save' , pad = (200 , 20) , size = (100,1) )],
    [sg.Listbox(task, size = (40,9) , font = ("Cambria" , 14) , key = 'tasklist' , background_color = "white" , pad = (100 , 20) , text_color = "black")],
    [sg.Button("Edit", font = ("Simplified Arabic Fixed", 14) , pad = (90 , 10) , size = (10,1)), sg.Button("Finish", font = ("Simplified Arabic Fixed", 14) , pad = (90 , 10),  size = (10,1))],
    [sg.Image("Creator.png", size=(720, 70))]

]

def add_tasks(values):
    if window.FindElement("add_save").GetText() == "Add":
        insert_into_table(values["task"],values["priority"])
        update_UI("0")
    else:
        oldtask = values['tasklist'][0]
        newtask = values['task']
        print(oldtask , newtask)
        pri = values['priority']
        change_task(oldtask,newtask,pri)
        window.FindElement('add_save').Update("Add")
        update_UI("0")

def update_UI(comp):

    tasks = select_all_records(comp)
    window.FindElement('tasklist').Update(values=tasks)
    window.FindElement('task').Update(value="")

def delete_tasks(values):
    mark_as_complete(values['tasklist'][0])
    update_UI("0")

def edit_tasks(values):
    window.FindElement('task').Update(value = values['tasklist'][0])
    window.FindElement('add_save').Update("Save")

def display_completed():
    update_UI("1")

def display_incomplete():
    update_UI("0")

if __name__ == '__main__':
    window = sg.Window("To Do List", layout, size=(600, 700))
    while True:
        events, values = window.Read()
        if events == sg.WINDOW_CLOSED:
            break

        if events == 'add_save':
            add_tasks(values)

        elif events == 'Delete':
            delete_tasks(values)

        elif events == 'Edit':
            edit_tasks(values)

        elif events == 'comp':
            display_completed()

        elif events == 'incomp':
            display_incomplete()

        else:
            break

    window.Close()