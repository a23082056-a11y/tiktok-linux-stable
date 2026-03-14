#!/usr/bin/env python3
import os
import sys

# Обманываем систему: говорим Qt не использовать GSSAPI/Kerberos
os.environ["QT_GSL_NO_GSSAPI"] = "1"

from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage

class TikTokWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TikTok Desktop (Flatpak)")
        self.resize(1100, 850)

        layout = QVBoxLayout()
        navbar = QHBoxLayout()

        btn_back = QPushButton("⬅ Назад")
        btn_back.clicked.connect(lambda: self.browser.back())
        btn_home = QPushButton("🏠 Главная")
        btn_home.clicked.connect(lambda: self.browser.setUrl(QUrl("https://www.tiktok.com")))
        btn_refresh = QPushButton("🔄 Обновить")
        btn_refresh.clicked.connect(lambda: self.browser.reload())

        navbar.addWidget(btn_back)
        navbar.addWidget(btn_home)
        navbar.addWidget(btn_refresh)
        navbar.addStretch()

        self.profile = QWebEngineProfile("TikTokProfile", self)
        self.profile.setHttpUserAgent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
        
        self.page = QWebEnginePage(self.profile, self)
        self.browser = QWebEngineView()
        self.browser.setPage(self.page)
        self.browser.setUrl(QUrl("https://www.tiktok.com"))

        layout.addLayout(navbar)
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TikTokWindow()
    window.show()
    sys.exit(app.exec())
