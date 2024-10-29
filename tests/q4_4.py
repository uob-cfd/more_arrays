test = {
  'name': 'Question 4_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you multipied and subtracted in the wrong
          >>> # order.
          >>> assert sum(celsius_max_temperatures) != 356705.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Did you remember to round to the nearest integer?
          >>> total = sum(celsius_max_temperatures)
          >>> assert (np.round(total) - total) == 0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert sum(celsius_max_temperatures) == 1280677.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert len(celsius_max_temperatures) == 65000
          >>> assert celsius_max_temperatures.item(2003) == 20.0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
