import requests
import pandas as pd




def request_api_data(start_date: str, end_date: str):
    '''
        This functing will return the json from
    '''
    API_LINK = f"https://api.open-meteo.com/v1/forecast?latitude=-6.254&longitude=106.7781&daily=temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,precipitation_sum,windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant,shortwave_radiation_sum,et0_fao_evapotranspiration&timezone=Asia%2FBangkok&start_date={ start_date }&end_date={ end_date }"
    json_return = requests.get(API_LINK).json()
    return json_return

if __name__ == '__main__':
    json_val = request_api_data('2023-02-13', '2023-10-23')
    df = pd.DataFrame(json_val['daily']).set_index('time')
    df.to_csv('data/weather20231023.csv')