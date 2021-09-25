import PyQt5.QtWidgets as Widgets
import PyQt5.QtCore as Core
import PyQt5.QtWebEngineWidgets as WebEW


class MyWebBrowser:
    
    def __init__(self) -> None:
        
        # main window
        self.window = Widgets.QWidget()
        self.window.setWindowTitle("Laurium Web Browser")
        
        # initializing layout and horizontal bar
        self.layout = Widgets.QVBoxLayout()
        self.horizontal = Widgets.QHBoxLayout()
        
        # url bar
        self.url_bar = Widgets.QTextEdit()
        self.url_bar.setMaximumHeight(30)
        self.url_bar.setMaximumWidth(1100)
        
        # go button
        self.go_btn = Widgets.QPushButton("Go")
        self.go_btn.setMinimumHeight(30)
        self.go_btn.setMaximumWidth(60)
        
        # back button
        self.back_btn = Widgets.QPushButton("<")
        self.back_btn.setMinimumHeight(30)
        self.back_btn.setMaximumWidth(30)
        
        # forward button
        self.forward_btn = Widgets.QPushButton(">")
        self.forward_btn.setMinimumHeight(30)
        self.forward_btn.setMaximumWidth(30)
        
        # adding url bar and navigation buttons to horizontal bar
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        
        # initializing web browser view
        self.browser = WebEW.QWebEngineView()
        
        # navigation buttons functions
        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        
        # adding horizontal bar and browser view to layout
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
        
        # default home page
        self.browser.setUrl(Core.QUrl("http://duckduckgo.com"))
        
        # set layout to main window and show it
        self.window.setLayout(self.layout)
        self.window.show()
    
    def navigate(self, url):
        """Navigate between pages

        Args:
            url (string): link to a website
        """
        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(Core.QUrl(url))
        
        
app = Widgets.QApplication([])
window = MyWebBrowser()
app.exec_()
        
