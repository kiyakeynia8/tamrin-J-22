import sys
from functools import partial
from database import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = Database()
        self.read_from_database()

        self.ui.btn_new_task.clicked.connect(self.new_tasks)

    def new_tasks(self):
        new_title = self.ui.tb_ne_task.text()
        new_description = self.ui.tb_n_t_d.toPlainText()
        feedback = self.db.add_new_task(new_title, new_description)

        if feedback == True:
            self.read_from_database()
            self.ui.tb_ne_task.setText("")
            self.ui.tb_n_t_d.setText("")

        else:
            msg_box = QMessageBox()
            msg_box.setText("مشکلی پیش امده!!")
            msg_box.exec_()

    def read_from_database(self):
        tasks = self.db.get_tasks()

        is_dons = []
        for i in range(len(tasks)):
            a = 1
            new_checkbox = QCheckBox()
            new_label = QLabel()
            new_btn = QPushButton("DEL")
            new_label.setText(tasks[i][1]) 
            
            self.ui.gl_tasks.addWidget(new_btn, i, 0)
            self.ui.gl_tasks.addWidget(new_checkbox, i, 1)
            self.ui.gl_tasks.addWidget(new_label, i, 2)
            new_checkbox.clicked.connect(partial(self.db.task_done, tasks[i][0]))
            new_btn.clicked.connect(partial(self.db.remove_task, tasks[i][0]))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec_()