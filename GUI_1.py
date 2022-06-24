from PyQt5 import QtWidgets
from GUI_2 import Ui_Dialog
from PyQt5.QtCore import pyqtSlot
from GUI_model_load import model_Predict
import sys

class ApplicationWindow(QtWidgets.QDialog):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Toxic Comment Classfication PyQt5 GUI')
        self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)
    @pyqtSlot()
    def on_pushButton_clicked(self):
        result = model_Predict(self.ui.lineEdit1.text())
        self.ui.label_3.setText(str("Toxic "+ "  "+ "  "+" : "+ "  "+ str(result[0][0]*100)+ "%"))
        self.ui.label_4.setText(str("Obscene : "+ "  "+ str(result[0][1] *100)+ "%"))
        self.ui.label_5.setText(str("Insult  "+ "  "+ "  "+": "+ "  "+ str(result[0][2]*100)+ "%"))
        
        if( ((result[0][0])*100)>=50 or ((result[0][1])*100)>=50 or ((result[0][2])*100)>=50):
            self.ui.label_6.setText(str("The comment contains strong language & will not be allowed to post it online!"))
        else:
            self.ui.label_6.setText(str("The comment does not contains strong language & will be allowed to post it online!"))
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
 