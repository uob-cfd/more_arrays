test = {
  'name': 'Question 5_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert difference_from_expected.size == 272
          >>> assert difference_from_expected.item(271) == abs(60 * 272 - sum(waiting_times))
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
