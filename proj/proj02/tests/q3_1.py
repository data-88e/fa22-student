test = {   'name': 'q3_1',
    'points': [0, 0, 0.1],
    'suites': [   {   'cases': [   {'code': '>>> indexed_data.labels == ("country", "year", "Indexed K", "Indexed L", "Indexed Y")\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> indexed_data.num_rows == 120\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(indexed_data.where("country", "China").where("year", 1990).column("Indexed K")[0], 14.5825)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
