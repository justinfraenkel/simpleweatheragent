import PySimpleGUI as sg
import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    return response.json()

def main():
    api_key = "beb3be6d521e740f37b6fc34cc2d46b8"  # Replace with your actual API key if needed

    # Define the window's layout
    layout = [
        [sg.Text("Enter a city name:"), sg.InputText(key='-CITY-')],
        [sg.Button('Get Weather'), sg.Button('Exit')],
        [sg.Text('', key='-OUTPUT-', size=(40, 3))]
    ]

    # Create the Window
    window = sg.Window('Weather AI', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Get Weather':
            city = values['-CITY-']
            weather_data = get_weather(city, api_key)
            
            if weather_data.get('cod') != 200:
                weather_info = f"Error: {weather_data.get('message', 'Unknown error')}"
            else:
                weather = weather_data['weather'][0]['description']
                temp = weather_data['main']['temp']
                weather_info = f"The weather in {city} is {weather} with a temperature of {temp}°C."
            
            window['-OUTPUT-'].update(weather_info)

    window.close()

if __name__ == "__main__":
    main()