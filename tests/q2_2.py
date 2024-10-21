test = {
  'name': 'Question 2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> # It looks like you didn't make an array.
          >>> assert type(book_title_words) == np.ndarray
          >>> # It looks like you included commas in the text.
          >>> # The three pieces of text in the array should be:
          >>> #   "Eats"
          >>> #   "Shoots"
          >>> #   "and Leaves"
          >>> assert not any([',' in text for text in book_title_words])
          >>> # It looks like you didn't include both words in the
          >>> # last piece of text.  It should be the actual string:
          >>> #   "and Leaves"
          >>> assert 'and ' in book_title_words.item(2)
          >>> assert np.all(book_title_words == ['Eats', 'Shoots', 'and Leaves'])
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
