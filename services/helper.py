from datetime import datetime, timedelta


class Helper():
    start_date = ''
    end_date = ''
    response_data = ''

    def set_response_data(self, response_data):
        if len(response_data) != 0:
            self.response_data = response_data

    def set_start_date(self, start_date):
        if len(start_date) != 0:
            self.start_date = start_date

    def set_end_date(self, end_date):
        if len(end_date) != 0:
            self.end_date = end_date

    def validate_date(self):
        # ----------------------------------------------------------------------------#
        # VERIFICAÇÃO DA DATA.
        # ----------------------------------------------------------------------------#
        try:
            datetime.strptime(self.start_date, '%d/%m/%Y')
            datetime.strptime(self.end_date, '%d/%m/%Y')
        except ValueError:
            raise ValueError("Data Informada está incorreta, deve ser DD/MM/YYYY")

        d_from_date = datetime.strptime(self.start_date, '%d/%m/%Y')
        d_to_date = datetime.strptime(self.end_date, '%d/%m/%Y')
        if abs((datetime.now() - d_from_date).days) > 7:
            raise ValueError('Data inicial maior que 7 dias')

        if abs((datetime.now() - d_to_date).days) > 7:
            raise ValueError('Data final maior que 7 dias')

        # ----------------------------------------------------------------------------#
        # FIM VERIFICAÇÃO.
        # ----------------------------------------------------------------------------#

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def clean_response_data(self):
        for data in self.response_data:
            return data
