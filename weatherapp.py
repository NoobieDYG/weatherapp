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
        self.temperature_label=QLabel(" ",self)
        self.emoji_label=QLabel(" ",self)
        self.description=QLabel(" ",self)
        self.feelslike=QLabel(" ",self)
        self.initUI()

        self.getweather.clicked.connect(self.get_weather)

    def initUI(self):
        self.setWindowTitle("Weather APP")

        vbox=QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_box)
        vbox.addWidget(self.getweather)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.feelslike)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description)
        

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_box.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description.setAlignment(Qt.AlignCenter)
        self.feelslike.setAlignment(Qt.AlignCenter)


        self.city_label.setObjectName('city_label')
        self.city_box.setObjectName('city_box')
        self.temperature_label.setObjectName('temperature_label')
        self.feelslike.setObjectName("feelslike")
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
                font-size: 50px;
            }
            QLabel#description{
                font-size: 50px;
                               
            }
            QLabel#emoji_label{
                font-size: 50px;
                font-family: Segoe UI Emoji;                   
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
            match response.status_code:
                case 400:
                    self.display_error("Bad request\nPlease check input")
                case 401:
                    self.display_error("Unauthorized\nCheck Key")
                case 403:
                    self.display_error("Access Denied\nOops")
                case 404:
                    self.display_error("Not Found\nWrong Input")
                case 500:
                    self.display_error("Server Error\n")
                case 502:
                    self.display_error("Bad Gateway\nOops")

        except requests.exceptions.RequestException as reqerror:
            self.display_error(f'Request error:\n{reqerror}')


    def display_error(self,msg):
        self.temperature_label.clear()
        self.feelslike.clear()
        self.description.clear()
        self.emoji_label.clear()
        self.temperature_label.setText(msg)
    
    def display_weather(self,data):
        #first displaying the temperature
        tempk=data['main']['temp']
        tempc=tempk-273.15
        self.temperature_label.setStyleSheet("font-size: 45px")
        self.temperature_label.setText(f"Temperature: {round(tempc,1)} C")
        #now displaying description
        descr=data['weather'][0]['description']
        self.description.setText(descr)
        self.description.setStyleSheet("font-size: 50px")
        #feels like
        feel=data['main']['feels_like']
        feel_in_C=feel-273.15
        self.feelslike.setStyleSheet("font-size: 45px")
        self.feelslike.setText(f"Feels Like: {round(feel_in_C,1)}")
        #emoji
        weather_id=data['weather'][0]['id']
        self.emoji_label.setText(self.weather_emoji(weather_id))
    @staticmethod
    def weather_emoji(weather_id):
        if weather_id>=200 and weather_id <=232:
            return "🌩️"
        elif 300<=weather_id<=321:
            return '⛅'
        elif 500<=weather_id<=531:
            return '🌧️'
        elif 600<=weather_id<=632:
            return '❄️'
        elif 701<=weather_id<=741:
            return '🌫️'
        


if __name__=="__main__":
    app=QApplication(sys.argv)
    weather_app=WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

