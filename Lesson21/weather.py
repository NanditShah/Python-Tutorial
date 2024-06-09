import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()


# pip install <package_name>
# pip install <package_name>=<package_version>
# pip uninstall <package_name>
# pip -U <package_name> //For upgrade
# pip list // List all the packages installed in that environment, if no environment then checkes for global
# pip freeze > <path_to_virtual_file_to_store_requirement_for_environment> // this will store all the required python packages with version detail, so other can download those packages when that projects gets cloned (SAME AS `package.json` in node environment)
# pip install -r <path_to_virtual_file_where_requirement_for_environment_are_stored>
# py -m venv <path_to_virtual_env_files>
# source <path_to_virtual_env_files/Scripts.activate> // to activate virtual environment
# deactivate // to deactivate virtual environment


def get_current_weather():
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name:\n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    print(request_url)

    weather_data = requests.get(request_url).json()

    # pprint(weather_data)

    print(f'\nCurrent weather for {weather_data["name"]}:')
    print(f'\nThe temp is {weather_data["main"]["temp"]:.1f}°')
    print(
        f'\n{weather_data["weather"][0]["description"].capitalize()} and feels like {weather_data["main"]["feels_like"]:.1f}°\n')


if __name__ == "__main__":
    get_current_weather()