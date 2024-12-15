import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class WebBrowser(QMainWindow):
    def __init__(self, url):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(url)
        self.setCentralWidget(self.browser)
        self.showFullScreen()  # Launch in fullscreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    url = QUrl("http://localhost:5000")  # Replace with your desired URL
    window = WebBrowser(url)
    sys.exit(app.exec_())

