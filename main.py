import asyncio
import sys
import threading
from datetime import datetime
import qasync
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        # setup UI interface python code
        self.ui.setupUi(self)
        qr = self.frameGeometry()
        # set center position for window on screen
        cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        # connect event to object for action click
        self.ui.AppendTextBtn.clicked.connect(self.click_btn_event)

    @qasync.asyncClose
    async def closeEvent(self, event):
        # example event for click on close window
        # we stop asyncio loop
        asyncio.get_event_loop().stop()

    @qasync.asyncSlot()
    async def click_btn_event(self):
        # read info from message input
        # with function text
        # in another object can used another function for read text
        message_text = self.ui.messageInput.text()
        # call function for write message on board
        await self.send_log(message_text)

    async def send_log(self, message):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        # MessagesBoard - name for QTextEdit
        self.ui.MessagesBoard.append(f"{current_time}: " + message)


if __name__ == "__main__":
    #create instance of application
    app = QApplication(sys.argv)
    #create loop for asyncio qasync
    loop = qasync.QEventLoop(app)
    asyncio.set_event_loop(loop)
    #create instance GUI
    ui = MainWindow()
    #show GUI
    ui.show()
    with loop:
        #run loop for work app in asyncio event loop
        loop.run_forever()
