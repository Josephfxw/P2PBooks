# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/Ui_UploadForm.ui'
#
# Created: Sat Nov 21 11:52:23 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(578, 186)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)
        self.submit_push_button = QtGui.QPushButton(Form)
        self.submit_push_button.setObjectName("submit_push_button")
        self.gridLayout.addWidget(self.submit_push_button, 5, 4, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.title_line_edit = QtGui.QLineEdit(Form)
        self.title_line_edit.setObjectName("title_line_edit")
        self.gridLayout.addWidget(self.title_line_edit, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.upload_push_button = QtGui.QPushButton(Form)
        self.upload_push_button.setObjectName("upload_push_button")
        self.gridLayout.addWidget(self.upload_push_button, 3, 4, 1, 1)
        self.genres_line_edit = QtGui.QLineEdit(Form)
        self.genres_line_edit.setObjectName("genres_line_edit")
        self.gridLayout.addWidget(self.genres_line_edit, 1, 2, 1, 1)
        self.price_spin_box = QtGui.QSpinBox(Form)
        self.price_spin_box.setMaximum(9999)
        self.price_spin_box.setObjectName("price_spin_box")
        self.gridLayout.addWidget(self.price_spin_box, 2, 2, 1, 1)
        self.author_line_edit = QtGui.QLineEdit(Form)
        self.author_line_edit.setObjectName("author_line_edit")
        self.gridLayout.addWidget(self.author_line_edit, 0, 4, 1, 1)
        self.isbn_line_edit = QtGui.QLineEdit(Form)
        self.isbn_line_edit.setObjectName("isbn_line_edit")
        self.gridLayout.addWidget(self.isbn_line_edit, 1, 4, 1, 1)
        self.file_location_label = QtGui.QLabel(Form)
        self.file_location_label.setObjectName("file_location_label")
        self.gridLayout.addWidget(self.file_location_label, 4, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.title_line_edit, self.author_line_edit)
        Form.setTabOrder(self.author_line_edit, self.genres_line_edit)
        Form.setTabOrder(self.genres_line_edit, self.isbn_line_edit)
        Form.setTabOrder(self.isbn_line_edit, self.price_spin_box)
        Form.setTabOrder(self.price_spin_box, self.upload_push_button)
        Form.setTabOrder(self.upload_push_button, self.submit_push_button)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "ISBN #", None, QtGui.QApplication.UnicodeUTF8))
        self.submit_push_button.setText(QtGui.QApplication.translate("Form", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Author", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Price", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Genres", None, QtGui.QApplication.UnicodeUTF8))
        self.upload_push_button.setText(QtGui.QApplication.translate("Form", "Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.file_location_label.setText(QtGui.QApplication.translate("Form", "File:", None, QtGui.QApplication.UnicodeUTF8))

