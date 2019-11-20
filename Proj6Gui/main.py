import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

list_of_numbers = []

class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('form.ui', self)

        self.setWindowTitle('Работа с массивами и файлами в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.loadFile_Btn.clicked.connect(self.upload_data)
        self.clear_Btn.clicked.connect(self.clear)
        self.ProcessData_Btn.clicked.connect(self.process_data)
        self.save_Btn.clicked.connect(self.save_data_in_file)

    def upload_data(self):
        global r_file

        r_file = QFileDialog.getOpenFileName(self, 'Открыть файл', '', "Text files (*.txt)")[0]

        if r_file:
            file = open(r_file, 'r')
            data = file.read()

            self.textEdit.appendPlainText("Полученные данные: \n" + data + "\n")

            value = ''

            for num in range(len(data)):
                if data[num].isdigit() or data[num] == '-':
                    value += data[num]
                else:
                    list_of_numbers.append(int(value))
                    value = ''


    def process_data(self):
        if validation_data():
            flag = find_minus()
            maximum = max(list_of_numbers)
            minimum = min(list_of_numbers)

            for i in range(len(list_of_numbers)):
                if maximum == list_of_numbers[i]:
                    list_of_numbers[i] += flag
                if minimum == list_of_numbers[i]:
                    list_of_numbers[i] += flag



            self.textEdit.appendPlainText('Обработанные данные:\n')
            count = 1
            for i in range(len(list_of_numbers)):
                self.textEdit.insertPlainText(str(list_of_numbers[i]) + " ")
                if count % 6 == 0:
                    self.textEdit.appendPlainText("")
                count += 1
        else:
            self.textEdit.appendPlainText("Неправильно введены данные! \n"
                                          "Таблица должна быть размером \n"
                                          "5х6 и состоять из чисел! \n")


    def save_data_in_file(self):
        if r_file:
            file = open(r_file.split(".")[0] + '-output.txt', 'w')

            count = 1
            for i in list_of_numbers:
                file.write(str(i) + ' ')
                if count % 6 == 0:
                    file.write("\n")
                count += 1

            file.close()
            self.textEdit.appendPlainText("Файл был успешно загружен! \n")
        else:
            self.textEdit.appendPlainText("Для начала загрузите файл!")


    def clear(self):
        self.textEdit.clear()

def validation_data():
    if len(list_of_numbers) == 30:
        for i in list_of_numbers:
            try:
                float(i)
            except Exception:
                return False
        return True
    else:
        return False

def find_minus():
    s = 0
    for i in list_of_numbers:
        if int(i) < 0:
            s += 1
    return s


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()