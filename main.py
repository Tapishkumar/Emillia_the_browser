import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forword_button = QAction('forword', self)
        forword_button.triggered.connect(self.browser.forward)
        navbar.addAction(forword_button)

        reload_button = QAction('reload', self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)

        home_button = QAction('Home', self)
        home_button.triggered.connect(self.home_page)
        navbar.addAction(home_button)

        self.urlBar = QLineEdit()
        self.urlBar.returnPressed.connect(self.go_to_Url)
        navbar.addWidget(self.urlBar)

        self.browser.urlChanged.connect(self.Url_Change)

    def home_page(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def go_to_Url(self):
        url = self.urlBar.text()
        self.browser.setUrl(QUrl(f"http://{url}.com"))

    def Url_Change(self, q):
        self.urlBar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName("Emilia")
winddow = mainWindow()
app.exec()
