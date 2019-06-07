import json

from models.climaTempo import Clima_Tempo
from ast import literal_eval


class ClimaTempoRepository():
    city_id = ''
    start_date = ''
    end_date = ''
    dates = ''
    response_data = ''

    def set_response_data(self, response_data):
        self.response_data = response_data

    def set_city_id(self, city_id):
        self.city_id = city_id

    def get_city_id(self):
        return self.city_id

    def set_start_date(self, start_date):
        if len(start_date) != 0:
            self.start_date = start_date

    def set_end_date(self, end_date):
        if len(end_date) != 0:
            self.end_date = end_date

    def save_data(self):
        teste = json.dumps(self.response_data['data'])
        data_json = literal_eval(teste)
        for n in data_json:
            save_data = {}
            save_data['date'] = n['date']
            save_data['probability'] = n['rain']['probability']
            save_data['precipitation'] = n['rain']['precipitation']
            save_data['max_day'] = n['temperature']['max']
            save_data['min_day'] = n['temperature']['min']
            save_data['city_id'] = self.response_data['id']
            save_data['name'] = self.response_data['name']
            save_data['state'] = self.response_data['state']
            save_data['country'] = self.response_data['country']
            print(save_data)
            Clima_Tempo.insert_many(save_data).execute()

    def get_data_results(self):
        data = []
        for n in Clima_Tempo.select().where(
                Clima_Tempo.max_day.between(Clima_Tempo.max_day, Clima_Tempo.max_day)).order_by(
            Clima_Tempo.max_day.desc()).limit(1).dicts():
            data.append(n)

        for t in Clima_Tempo.select().where(
                Clima_Tempo.min_day.between(Clima_Tempo.min_day, Clima_Tempo.min_day)).order_by(
            Clima_Tempo.min_day.asc()).limit(1).dicts():
            data.append(t)

        for p in Clima_Tempo.select().where(
                Clima_Tempo.probability.between(Clima_Tempo.probability, Clima_Tempo.probability)).order_by(
            Clima_Tempo.probability.desc()).limit(1).dicts():
            data.append(p)

        return data
