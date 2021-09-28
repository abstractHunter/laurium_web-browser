import PyQt5.QtWidgets as Widgets
import PyQt5.QtCore as Core
import PyQt5.QtWebEngineWidgets as WebEW

import sys


class MyWebBrowser:
    
    def __init__(self) -> None:
        
        # main window
        self.window = Widgets.QWidget()
        self.window.setWindowTitle("Laurium Web Browser")
        
        # initializing layout and horizontal bar
        self.layout = Widgets.QVBoxLayout()
        self.horizontal = Widgets.QHBoxLayout()
        
        # url bar
        self.url_bar = Widgets.QLineEdit()
        self.url_bar.setToolTip("Enter Page Url")
        self.url_bar.setMaximumHeight(30)
        self.url_bar.setMaximumWidth(1000)
        self.url_bar.setMinimumWidth(400)
        
        # go button
        self.go_btn = Widgets.QPushButton("Go")
        self.go_btn.setToolTip("Go to Link")
        self.go_btn.setMinimumHeight(30)
        self.go_btn.setMaximumWidth(60)
        
        # back button
        self.back_btn = Widgets.QPushButton("<")
        self.back_btn.setToolTip("Go to the Previous Page")
        self.back_btn.setMinimumHeight(30)
        self.back_btn.setMaximumWidth(30)
        
        # forward button
        self.forward_btn = Widgets.QPushButton(">")
        self.forward_btn.setToolTip("Go to the Next Page")
        self.forward_btn.setMinimumHeight(30)
        self.forward_btn.setMaximumWidth(30)
        
        # reload button
        self.reload_btn = Widgets.QPushButton("R")
        self.reload_btn.setToolTip("Reload Page")
        self.reload_btn.setMinimumHeight(30)
        self.reload_btn.setMaximumWidth(30)
        
        # home button
        self.home_btn = Widgets.QPushButton("H")
        self.home_btn.setToolTip("Go to Home")
        self.home_btn.setMinimumHeight(30)
        self.home_btn.setMaximumWidth(30)
        
        # menu button
        self.menu_btn = Widgets.QPushButton("M")
        self.menu_btn.setToolTip("Open Menu")
        self.menu_btn.setMinimumHeight(30)
        self.menu_btn.setMaximumWidth(30)
        
        # adding url bar and buttons to horizontal bar
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.reload_btn)
        self.horizontal.addWidget(self.home_btn)
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.menu_btn)
        
        # initializing web browser view
        self.browser = WebEW.QWebEngineView()
        
        # navigation buttons functions
        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.text()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.reload_btn.clicked.connect(self.browser.reload)
        self.home_btn.clicked.connect(lambda: self.navigate("http://duckduckgo.com"))
        
        # load url when ENTER BUTTON is pressed
        self.url_bar.returnPressed.connect(lambda: self.navigate(self.url_bar.text()))
        
        # adding horizontal bar and browser view to layout
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
        
        
        # style sheet
        self.window.setStyleSheet("""
                QWidget {
                    background-color: rgb(48, 48, 48);
                    color: rgb(240, 240, 240);
                }
                QPushButton {
                    background: rgb(70, 70, 70);
                    width: 30px;
                    padding: 5px;
                    border-radius: 10px;
                }
                QPushButton:hover {
                    background: rgb(120, 120, 120)
                }
        """)
        
        
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
        
        
app = Widgets.QApplication(sys.argv)
app.setApplicationName("Laurium Web Browser")
app.setApplicationVersion("2.0.0")
window = MyWebBrowser()
app.exec_()
        