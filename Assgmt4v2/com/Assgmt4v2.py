'''
Created on 22 Apr 2019

@author: mandla_
'''

import sys
import sqlite3
from sqlite3 import Error
from PyQt5.QtWidgets import QMainWindow, QApplication
from Assgmt4ui import Ui_MainWindow 


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.subwindow.show()
        self.ui.subwindow_2.show()
        self.ui.subwindow_3.show()
        
        self.ui.menubar.setNativeMenuBar(False)
        self.setWindowTitle('''CSET Community Engagement Programme''')
        self.ui.actionAdd_New_Record.triggered.connect(self.addNewRec)
        self.ui.subW2_login_btn.clicked.connect(self.dbLogin)
        self.show()
    
    def cascadeArrange(self):
        self.ui.mdiArea.cascadeSubWindows() 
        
    def tileArrange(self):
        self.ui.mdiArea.tileSubWindows()
        
    def addNewRec(self): 
        ''' If user clicked "Add new record '''
        
        database = ('/users/mandla_/Documents/cmeprojects.db')
        
        try:
            dbConnection = sqlite3.connect(database)
            cursr = dbConnection.cursor()
            cursr.execute('''SELECT * FROM projects''')
            rows = cursr.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(e)
        finally:
            if dbConnection:
                dbConnection.close()
    
    
    def loginSuccess(self):
        message = '''Login successful'''
        self.ui.subW2_loginMessage_lbl.text = message
    
    
    
    def loginFail(self):
        message = '''Login failed'''
        self.ui.subW2_loginMessage_lbl.text = message           
    
    
    def dbLogin(self):
        username = self.ui.subW2_userName_ledit.text()
        password = self.ui.subW2_password_ledit.text()
        db = ('/users/mandla_/Documents/cmeprojects.db')
        
        try:
            connection = sqlite3.connect(db)
            cur = connection.cursor()
            cur.execute('''SELECT Password FROM Members''')
            passVal = cur.fetchall()
            cur.execute('''SELECT FullName FROM Members''')
            nameVal = cur.fetchall()
            
            if (passVal == password) and (username == nameVal):
                loginSuccess()
            else:
                loginFail()
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())