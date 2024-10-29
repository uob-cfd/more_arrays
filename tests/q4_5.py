test = {
  'name': 'Question 4_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert len(celsius_temperature_ranges) == 65000
          >>> assert celsius_temperature_ranges.item(1) == 10
          >>> assert round(sum(celsius_temperature_ranges)) == 768351
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
