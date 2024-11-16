import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label=QLabel("Enter City Name: ",self)
        self.city_box=QLineEdit(self)
        self.getweather=QPushButton("Get Weather",self)
        self.temperature_label=QLabel("70F",self)
        self.emoji_label=QLabel(" emo ",self)
        self.description=QLabel("Sunny",self)
        self.initUI()

        self.get_weather_button.clicked.connect(self.get_weather)

    def initUI(self):
        self.setWindowTitle("Weather APP")

        vbox=QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_box)
        vbox.addWidget(self.getweather)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_box.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description.setAlignment(Qt.AlignCenter)


        self.city_label.setObjectName('city_label')
        self.city_box.setObjectName('city_box')
        self.temperature_label.setObjectName('temperature_label')
        self.emoji_label.setObjectName('emoji_label')
        self.description.setObjectName('description')
        self.getweather.setObjectName('getweather')


        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: calibri;
            }
            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_box {
                font-size: 40px;
            }
            QPushButton#get_weather {
                font-size: 100px;
                font-weight: bold;
            }
            QLabel#temperature_label {
                font-size: 75px;
            }
            QLabel#description{
                font-size: 100px;
                               
            }
        """)

    def get_weather(self):
        print("Weahter ")




if __name__=="__main__":
    app=QApplication(sys.argv)
    weather_app=WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
