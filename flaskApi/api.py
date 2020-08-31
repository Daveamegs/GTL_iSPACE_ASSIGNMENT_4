from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class CovidCases(Resource):
    def get(self):
        return {
            'Ghana': {
                'Total Cases': 10900,
                'Active Cases': 3720,
                'Recovered': 6938,
                'Total Death': 109
            },
            'Nigeria': {
                'Total Cases': 65900,
                'Active Cases': 35829,
                'Recovered': 29909,
                'Total Death': 1182
            },
            'Ivory Coast': {
                'Total Cases': 8765,
                'Active Cases': 3806,
                'Recovered': 4695,
                'Total Death': 204
            },
            'Togo': {
                'Total Cases': 231,
                'Active Cases': 58,
                'Recovered': 122,
                'Total Death': 8
            },
            'Sudan': {
                'Total Cases': 97,
                'Active Cases': 32,
                'Recovered': 45,
                'Total Death': 4
            },
            'Gambia': {
                'Total Cases': 287,
                'Active Cases': 106,
                'Recovered': 132,
                'Total Death': 23
            },
            'Uganda': {
                'Total Cases': 312,
                'Active Cases': 121,
                'Recovered': 176,
                'Total Death': 11
            },
            'Senegal': {
                'Total Cases': 765,
                'Active Cases': 65,
                'Recovered': 700,
                'Total Death': 0
            },
            'Algeria': {
                'Total Cases': 8995,
                'Active Cases': 5002,
                'Recovered': 2345,
                'Total Death': 221
            }
        }


api.add_resource(CovidCases, '/')

if __name__ == '__main__':
    app.run(debug=True)
