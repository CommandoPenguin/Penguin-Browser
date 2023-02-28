import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

app = QApplication(sys.argv)
webview = QWebEngineView()

mainwindow = QMainWindow()
mainwindow.setWindowTitle('Penguin Browser')
mainwindow.setCentralWidget(webview)

toolbar = QToolBar()
mainwindow.addToolBar(toolbar)

back_button = QAction('Back', toolbar)
back_button.triggered.connect(webview.back)
toolbar.addAction(back_button)

forward_button = QAction('Forward', toolbar)
forward_button.triggered.connect(webview.forward)
toolbar.addAction(forward_button)

reload_button = QAction('Reload', toolbar)
reload_button.triggered.connect(webview.reload)
toolbar.addAction(reload_button)

webview.load(QUrl('https://www.google.com'))
mainwindow.show()
sys.exit(app.exec_())
