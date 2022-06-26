from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
from playsound import *
import pymysql
from PyQt5.QtWidgets import QMessageBox
from tkinter import *
from tkinter import messagebox, ttk
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QDialog,QApplication,QFileDialog,QAbstractItemView
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5.QtCore import Qt


class Ui_cloud_contact(object):
    def __init__(self):
            self.root =Tk()
            self.root.title("List of Contacts")
            self.root.configure(width=300, height=300)
            self.root.configure(bg='lightgray')
            self.tree = ttk.Treeview(self.root, columns=("id","name","phone number",))
            self.tree.heading('#0', text='id')
            self.tree.column('#0', width=50)
            self.tree.heading('#1', text='name')
            self.tree.column('#1', width=150)
            self.tree.heading('#2', text='phone number')
            self.tree.column('#2', width=150)
            self.tree.pack()
            Button(self.root, text='back', command=self.root.withdraw).pack()
            self.root.withdraw()
            
            try:
                    self.mydb = pymysql.connect(host="localhost",user="root",passwd="root",database='arvin')
                    print('Connected')
            except:
                    messagebox.showerror("Connection failed", "Please Check your internet Connection")                    
            try:
                    self.mycursor = self.mydb.cursor()
                    query = "CREATE TABLE IF NOT EXISTS `arvin`.`contact_list` (`id` INT NOT NULL AUTO_INCREMENT,`name` VARCHAR(15) NOT NULL,`phone_number` VARCHAR(13) NOT NULL,PRIMARY KEY (`id`),UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,UNIQUE INDEX `phone_number_UNIQUE` (`phone_number` ASC) VISIBLE);"
                    self.mycursor.execute(query)      
                    print("Done!")
            except:
                    messagebox.showerror("Connection failed", "Please Check your internet Connection")
            
             
       
         
             
        
    def close_all(self):
             if self.actionExit.triggered:
                QApplication.quit()    
              
            
                    
        
        
    def sound1(self):
        playsound('amogos.mp3')     
        
        
    def sound2(self):
        playsound('aughh.mp3')  
        
        
    
            
    def show_all_contacts(self):
        query="SELECT * FROM `arvin`.`contact_list`;"
        self.mycursor.execute(query)
        result = self.mycursor.fetchall()
        Values=[]
        
    def search_button_method(self):

            self.root.deiconify()
            self.query = "SELECT * FROM `arvin`.`contact_list` WHERE `name` LIKE %s;" 
            self.mycursor.execute(self.query, "%"+self.name1.text()+"%")
            result = self.mycursor.fetchall()
            self.tree.delete(*self.tree.get_children())
            for contacts in result:
                name = contacts[1]
                phone_number = contacts[2]                
                self.tree.insert('', 'end', text=contacts[0],values=(name, phone_number))
                
                    
            
            
            
            
                 
            
    def add_btn(self):
            query = "INSERT INTO `arvin`.`contact_list` (`name`,`phone_number`) VALUES (%s, %s);"
            values = self.name1.text(), self.phone_number1.text()   
            self.mycursor.execute(query,values)
            self.mydb.commit()                           
            messagebox.showinfo("Success😄", f"Contact {self.name1.text()} added successfully😉.")
            
    
        
            
     
            
    def setupUi(self, cloud_contact):
        cloud_contact.setObjectName("cloud_contact")
        cloud_contact.resize(639, 464)
        self.centralwidget = QtWidgets.QWidget(cloud_contact)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 651, 481))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setPixmap(QtGui.QPixmap("pic.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.add_contact_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_contact_button.setGeometry(QtCore.QRect(240, 250, 151, 41))
        self.add_contact_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_contact_button.setMouseTracking(False)
        self.add_contact_button.clicked.connect(self.add_btn)                  #hey its here :)
        self.add_contact_button.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.add_contact_button.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(255, 170, 255);\n"
"\n"
"\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.add_contact_button.setObjectName("add_contact_button")
        self.name1 = QtWidgets.QLineEdit(self.centralwidget)
        self.name1.setGeometry(QtCore.QRect(240, 120, 141, 20))
        self.name1.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.name1.setObjectName("name1")
        self.phone_number1 = QtWidgets.QLineEdit(self.centralwidget)
        self.phone_number1.setGeometry(QtCore.QRect(240, 180, 141, 21))
        self.phone_number1.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.phone_number1.setObjectName("phone_number1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 20, 61, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("person.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(240, 310, 151, 41))
        self.search_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_button.setMouseTracking(False)
        self.search_button.clicked.connect(self.search_button_method)
        
        self.search_button.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.search_button.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(255, 170, 255);\n"
"\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.search_button.setObjectName("search_button")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(10, 10, 221, 401))
        self.treeView.setObjectName("treeView")
        self.treeView.hide()                            #i hide this shit here dont forget
        
        cloud_contact.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(cloud_contact)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 21))
        self.menubar.setObjectName("menubar")
        self.menuChange = QtWidgets.QMenu(self.menubar)
        self.menuChange.setObjectName("menuChange")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        cloud_contact.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(cloud_contact)
        self.statusbar.setObjectName("statusbar")
        cloud_contact.setStatusBar(self.statusbar)
        self.actionSearch = QtWidgets.QAction(cloud_contact)
        self.actionSearch.setObjectName("actionSearch")
        self.actionabout_developer = QtWidgets.QAction(cloud_contact)
        self.actionAdd = QtWidgets.QAction(cloud_contact)
        self.actionAdd.setObjectName("actionAdd")
        self.actionExit = QtWidgets.QAction(cloud_contact)
        self.actionExit.setObjectName("actionExit")
        self.actionabout_developer.setObjectName("actionAbout_developer")
        self.actionSecret_Button = QtWidgets.QAction(cloud_contact)
        self.actionSecret_Button.setObjectName("actionSecret_Button")
        self.actionYou_can_click_me_to = QtWidgets.QAction(cloud_contact)
        self.actionYou_can_click_me_to.setObjectName("actionYou_can_click_me_to")
        self.action = QtWidgets.QAction(cloud_contact)
        self.action.setObjectName("action")
        self.menuChange.addAction(self.actionExit)
        self.menu.addAction(self.actionSecret_Button)
        self.menu.addAction(self.actionYou_can_click_me_to)
        self.menubar.addAction(self.menuChange.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.actionSecret_Button.triggered.connect(self.sound1)     #54737584838
        self.actionYou_can_click_me_to.triggered.connect(self.sound2)
        
                                    
        self.retranslateUi(cloud_contact)
        QtCore.QMetaObject.connectSlotsByName(cloud_contact)

    def retranslateUi(self, cloud_contact):
        _translate = QtCore.QCoreApplication.translate
        cloud_contact.setWindowTitle(_translate("cloud_contact", "Cloud_contact"))
        self.add_contact_button.setText(_translate("cloud_contact", "Add Contact"))
        self.name1.setPlaceholderText(_translate("cloud_contact", "Name"))
        self.phone_number1.setPlaceholderText(_translate("cloud_contact", "Phone number"))
        self.search_button.setText(_translate("cloud_contact", "Search"))
        self.menuChange.setTitle(_translate("cloud_contact", "Change "))
        self.menu.setTitle(_translate("cloud_contact", "Suprize me "))
        self.actionSearch.setText(_translate("cloud_contact", "Search"))
        self.actionAdd.setText(_translate("cloud_contact", "Add"))
        self.actionabout_developer.setText(_translate("cloud_contact", "About Developer"))
        self.actionExit.setText(_translate("cloud_contact", "Exit"))
        self.actionSecret_Button.setText(_translate("cloud_contact", "Click me :)"))
        self.actionYou_can_click_me_to.setText(_translate("cloud_contact", "You can click me to :)"))
        self.action.setText(_translate("cloud_contact", "Just click :)"))
        self.actionExit.triggered.connect(self.close_all)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cloud_contact = QtWidgets.QMainWindow()
    ui = Ui_cloud_contact()
    ui.setupUi(cloud_contact)
    cloud_contact.show()
    ui.root.mainloop()
    sys.exit(app.exec_())