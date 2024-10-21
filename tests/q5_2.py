test = {
  'name': 'Question 5_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # The decrease should be a positive number.
          >>> assert biggest_decrease > 0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Hint: biggest decrease is above 30, but not 47.
          >>> assert 30 <= biggest_decrease < 47
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
