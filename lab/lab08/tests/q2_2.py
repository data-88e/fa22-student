test = {   'name': 'q2_2',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> assert type(q_1) == sympy.Symbol, "q_1 should be a Sympy symbol"\n'
                                               '>>> assert type(q_2) == int, "q_1 should be a number"\n'
                                               '>>> assert type(P) == sympy.Symbol, "P should be a Sympy symbol"\n'
                                               '>>> assert type(c) == int, "c should be a number"\n'
                                               '>>> assert q_1 in profit_function.as_coefficients_dict(), "q_1 should be a variable in profit_function"\n'
                                               '>>> assert P not in profit_function.as_coefficients_dict(), "P cannot be a variable in profit_function"\n'
                                               '>>> assert len(profit_function.as_coefficients_dict()) == 2\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
