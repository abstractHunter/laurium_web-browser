import PyQt5.QtWidgets as Widgets
import PyQt5.QtCore as Core
import PyQt5.QtWebEngineWidgets as WebEW

import sys


class MyWebBrowser(Widgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MyWebBrowser, self).__init__(*args, **kwargs)
        
        
         # creating a tab widget
        self.tabs = Widgets.QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        self.tabs.setMinimumWidth(700)
        self.setCentralWidget(self.tabs)
        
        # creating a tool bar for navigation
        nav_bar = Widgets.QToolBar("Navigation")
        nav_bar.setIconSize(Core.QSize(16, 16))
        self.addToolBar(nav_bar)
        
        # adding back action
        back_btn = Widgets.QAction("<", self)
        back_btn.setToolTip("Back to previous page")
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        nav_bar.addAction(back_btn)
  
        # adding next button
        next_btn = Widgets.QAction(">", self)
        next_btn.setToolTip("Forward to next page")
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        nav_bar.addAction(next_btn)
  
        # adding reload button
        reload_btn = Widgets.QAction("R", self)
        reload_btn.setToolTip("Reload page")
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        nav_bar.addAction(reload_btn)
  
        # adding home action
        home_btn = Widgets.QAction("H", self)
        home_btn.setToolTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        nav_bar.addAction(home_btn)
        
        # adding a separator
        nav_bar.addSeparator()
  
        # creating a line edit widget for URL
        self.urlbar = Widgets.QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        self.urlbar.setMaximumWidth(1000)
        nav_bar.addWidget(self.urlbar)
  
        # adding stop action
        stop_btn = Widgets.QAction("X", self)
        stop_btn.setToolTip("Stop loading current page")
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        nav_bar.addAction(stop_btn)
        
        # adding menu button
        menu_btn = Widgets.QAction("M", self)
        menu_btn.setToolTip("Open Browser Menu")
        nav_bar.addAction(menu_btn)
        
        # styling the windows
        self.setStyleSheet("""
            QWidget {
                background-color: rgb(48, 48, 48);
                color: rgb(240, 240, 240);
                border: 0;
            }
            QToolBar {
                border-bottom: 1px solid rgb(100, 100, 100);
            }
            QToolButton, QTabBar::tab {
                background: rgb(70, 70, 70);
                border-radius: 10px;
                min-width: 2ex;
                min-height: 2ex;
                padding: 5px;
                margin: 2px;
                color: rgb(255, 255, 255);
            }
            QToolButton:hover, QTabBar::tab:hover {
                background: rgb(90, 90, 90);
            }
            QLineEdit {
                min-width: 2ex;
                font-size: 14px;
                background-color: rgb(36, 36, 36);
                color: rgb(240, 240, 240);
                border: 2px solid rgb(70, 70, 70);
                border-radius: 10px;
                padding: 5px;
                margin: 10px;
            }
        """)
        
        # creating first tab
        self.add_new_tab(Core.QUrl('http://www.google.com'), 'Homepage')
  
        # showing all the components
        self.show()
  
        # setting window title
        self.setWindowTitle("Laurium Web Browser")
        
        

    def add_new_tab(self, qurl = None, label ="Blank"):
          
        if qurl is None:  # if url is blank
            qurl = Core.QUrl('https://www.google.com')
  
        # creating a QWebEngineView object
        browser = WebEW.QWebEngineView()
        browser.setUrl(qurl)
  
        # setting tab index
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)
  
        # adding action to the browser when url is changed
        # update the url
        browser.urlChanged.connect(lambda qurl, browser = browser:
                                   self.update_urlbar(qurl, browser))
  
        # adding action to the browser when loading is finished
        # set the tab title
        browser.loadFinished.connect(lambda _, i = i, browser = browser:
                                     self.tabs.setTabText(i, browser.page().title()))
  
    # when double clicked on tabs
    def tab_open_doubleclick(self, i):
        if i == -1:
            self.add_new_tab()
  
    # when tab is changed
    def current_tab_changed(self, i):
        qurl = self.tabs.currentWidget().url()  # get the current url
        self.update_urlbar(qurl, self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())
  
    # when tab is closed
    def close_current_tab(self, i):
        if self.tabs.count() < 2:  # if there is only one tab
            # do nothing
            return
  
        self.tabs.removeTab(i)  # else remove the tab
  
    # method for updating the title
    def update_title(self, browser):       
        if browser != self.tabs.currentWidget():  # if signal is not from the current tab
            # do nothing
            return
  
        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle("% s - Laurium Web Browser" % title)
  
    # action to go to home
    def navigate_home(self):
        self.tabs.currentWidget().setUrl(Core.QUrl("http://www.google.com"))
  
    # method for navigate to url
    def navigate_to_url(self):
  
        # get the line edit text and convert it to QUrl object
        qurl = Core.QUrl(self.urlbar.text())

        if qurl.scheme() == "":
            qurl.setScheme("http")
  
        self.tabs.currentWidget().setUrl(qurl)
  
    # method to update the url
    def update_urlbar(self, qurl, browser = None):
        # If this signal is not from the current tab, ignore
        if browser != self.tabs.currentWidget():
            return

        self.urlbar.setText(qurl.toString())
        self.urlbar.setCursorPosition(0)
  

app = Widgets.QApplication(sys.argv)
app.setApplicationName("Laurium Web Browser")
app.setApplicationVersion("3.0.0")
window = MyWebBrowser()

app.exec_()
