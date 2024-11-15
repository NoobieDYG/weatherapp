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


if __name__=="__main__":
    app=QApplication(sys.argv)
    weather_app=WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())