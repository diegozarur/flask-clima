from config import BaseConfiguration
from ast import literal_eval
import requests
from repositories.ClimaTempoRepository import ClimaTempoRepository

data_repository = ClimaTempoRepository()


class ApiService():

    def __init__(self, city):
        self.city = city

        response = requests.get(BaseConfiguration.API_HOST_CITY.format(self.city))

        if response.status_code == 200 and len(response.json()) != 0:
            data_json = literal_eval(str(response.json()).strip('[').strip(']'))
            data_repository.set_city_id(data_json['id'])

        if response.status_code == 404 or len(response.json()) == 0:
            raise ValueError('ID para a cidade ' + self.city + ' não foi encontrado, Favor verificar o nome da Cidade')

    def forecast_days_city(self):
        if len(data_repository.get_data_results()) != 0:
            return data_repository.get_data_results()

        response = requests.get(BaseConfiguration.API_HOST_FORECAST.format(data_repository.get_city_id()))
        if response.status_code == 200 and len(response.json()) != 0:
            data_repository.set_response_data(response.json())
            data_repository.save_data()

        elif response.status_code == 404:
            return 'Not Found.'

    def get_results(self):
        return ClimaTempoRepository().get_data_results()
