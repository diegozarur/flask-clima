from flask import Flask, request, jsonify
from services.helper import Helper
from services.api_service import ApiService

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
helper_date = Helper()


# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#
@app.route('/clima/<cidade>', methods=['GET'])
def get_city_info(cidade):
    if request.args.get('start_date') and request.args.get('end_date'):
        s_date = request.args.get('start_date')
        e_date = request.args.get('end_date')
        helper_date.set_start_date(s_date)
        helper_date.set_end_date(e_date)
        helper_date.validate_date()

        data = ApiService(cidade)
        data.forecast_days_city()
        return jsonify(data.get_results()), 200
    return jsonify({'success': False, 'data': 'Falta Alguma data, no parâmetro da url'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002', debug=True)
