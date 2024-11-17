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
        self.emoji_label=QLabel(" ☀️ ",self)
        self.description=QLabel("Sunny",self)
        self.initUI()

        self.getweather.clicked.connect(self.get_weather)

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
            QPushButton#getweather {
                font-size: 40px;
                font-weight: bold;
            }
            QLabel#temperature_label {
                font-size: 75px;
            }
            QLabel#description{
                font-size: 50px;
                               
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;                   
            }
        """)

    def get_weather(self):
        
        api_key="enter_your_api_key"
        city_name=self.city_box.text()
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

        try:
            response=requests.get(url)
            response.raise_for_status()
            data=response.json()

            if data["cod"]==200:
                self.display_weather(data)
                
        except requests.exceptions.HTTPError:
            print(response.status_code)
        except requests.exceptions.RequestException:
            pass


    def display_error(self,msg):
        pass
    
    def display_weather(self,data):
        print(data)


if __name__=="__main__":
    app=QApplication(sys.argv)
    weather_app=WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

