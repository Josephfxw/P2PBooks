# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/Ui_ReaderForm.ui'
#
# Created: Thu Nov 26 21:04:26 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(498, 203)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.title_line_edit = QtGui.QLineEdit(Form)
        self.title_line_edit.setObjectName("title_line_edit")
        self.gridLayout.addWidget(self.title_line_edit, 0, 2, 1, 1)
        self.report_push_button = QtGui.QPushButton(Form)
        self.report_push_button.setObjectName("report_push_button")
        self.gridLayout.addWidget(self.report_push_button, 3, 3, 1, 1)
        self.pdf_reader_path_label = QtGui.QLabel(Form)
        self.pdf_reader_path_label.setText("")
        self.pdf_reader_path_label.setObjectName("pdf_reader_path_label")
        self.gridLayout.addWidget(self.pdf_reader_path_label, 6, 1, 1, 2)
        self.ratings_line_edit = QtGui.QLineEdit(Form)
        self.ratings_line_edit.setObjectName("ratings_line_edit")
        self.gridLayout.addWidget(self.ratings_line_edit, 1, 2, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.uploader_by_line_edit = QtGui.QLineEdit(Form)
        self.uploader_by_line_edit.setObjectName("uploader_by_line_edit")
        self.gridLayout.addWidget(self.uploader_by_line_edit, 2, 2, 1, 1)
        self.browse_pdf_reader_push_button = QtGui.QPushButton(Form)
        self.browse_pdf_reader_push_button.setObjectName("browse_pdf_reader_push_button")
        self.gridLayout.addWidget(self.browse_pdf_reader_push_button, 6, 3, 1, 1)
        self.time_remaining_label = QtGui.QLabel(Form)
        self.time_remaining_label.setText("")
        self.time_remaining_label.setObjectName("time_remaining_label")
        self.gridLayout.addWidget(self.time_remaining_label, 4, 2, 1, 1)
        self.read_pause_push_button = QtGui.QPushButton(Form)
        self.read_pause_push_button.setObjectName("read_pause_push_button")
        self.gridLayout.addWidget(self.read_pause_push_button, 3, 0, 1, 3)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.checkout_at_label = QtGui.QLabel(Form)
        self.checkout_at_label.setText("")
        self.checkout_at_label.setObjectName("checkout_at_label")
        self.gridLayout.addWidget(self.checkout_at_label, 5, 1, 1, 2)
        self.review_rate_push_button = QtGui.QPushButton(Form)
        self.review_rate_push_button.setObjectName("review_rate_push_button")
        self.gridLayout.addWidget(self.review_rate_push_button, 2, 3, 1, 1)
        self.share_push_button = QtGui.QPushButton(Form)
        self.share_push_button.setObjectName("share_push_button")
        self.gridLayout.addWidget(self.share_push_button, 0, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Reader", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Uploader", None, QtGui.QApplication.UnicodeUTF8))
        self.report_push_button.setText(QtGui.QApplication.translate("Form", "Report", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Ratings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Time remaining", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "PDF Reader", None, QtGui.QApplication.UnicodeUTF8))
        self.browse_pdf_reader_push_button.setText(QtGui.QApplication.translate("Form", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.read_pause_push_button.setText(QtGui.QApplication.translate("Form", "Read/Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Checked out", None, QtGui.QApplication.UnicodeUTF8))
        self.review_rate_push_button.setText(QtGui.QApplication.translate("Form", "Review/Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.share_push_button.setText(QtGui.QApplication.translate("Form", "Share", None, QtGui.QApplication.UnicodeUTF8))

