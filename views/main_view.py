from PySide import QtGui
from ui import Ui_UploadForm, Ui_MainWindowVisitor


class UploadFormView(QtGui.QWidget):
    def __init__(self, model):
        self.model = model
        super(UploadFormView, self).__init__()
        self.ui = Ui_UploadForm.Ui_Form()
        self.build_ui()

    def build_ui(self):
        self.ui.setupUi(self)
        # Disable text edit and also put a temporary message
        self.ui.preview_text_edit.setText('Please click upload to show preview.')
        self.ui.preview_text_edit.setDisabled(True)

        # Connect buttons to functions
        self.ui.upload_push_button.clicked.connect(self.submit)

    def submit(self):
        self.ui.preview_text_edit.setText('P SUONG')


class MainWindowVisitorView(QtGui.QMainWindow):
    def __init__(self, model):
        self.model = model
        super(MainWindowVisitorView, self).__init__()
        self.ui = Ui_MainWindowVisitor.Ui_MainWindow()
        self.build_ui()

    def build_ui(self):
        self.ui.setupUi(self)

        # Hide results table widget for later
        self.ui.search_table_widget.hide()
        self.ui.close_push_button.hide()

        self.ui.go_push_button.clicked.connect(self.search)
        self.ui.close_push_button.clicked.connect(self.close_search)

    def search(self):
        self.ui.search_table_widget.show()
        self.ui.close_push_button.show()

    def close_search(self):
        self.ui.search_table_widget.hide()
        self.ui.close_push_button.hide()
