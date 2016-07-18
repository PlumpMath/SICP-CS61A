test = {
  'name': 'Odds and Evens',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class OddNaturalsIterator():
          ...     def __init__(self):
          ...         self.current = 1
          ...     def __next__(self):
          ...         result = self.current
          ...         self.current += 2
          ...         return result
          ...     def __iter__(self):
          ...         return self
          >>> odds = OddNaturalsIterator()
          >>> odd_iter1 = iter(odds)
          >>> odd_iter2 = iter(odds)
          >>> next(odd_iter1)
          94ce22b5936436a75abf185df37ba826
          # locked
          >>> next(odd_iter1)
          350815b30c2ebeb01da1870d87346e85
          # locked
          >>> next(odd_iter1)
          9934e055a74f1f7f5fb94c0f9fd6402d
          # locked
          >>> next(odd_iter2)
          3f8f8f09d1f65fa9740c33b3c16d4731
          # locked
          >>> next(odd_iter1)
          b1cf566efb20d5b4e8e0fcba34deeb5f
          # locked
          >>> next(odd_iter2)
          7770d7151426f0a15dc7d17154603e7b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> class EvenNaturalsIterator():
          ...     def __init__(self):
          ...         self.current = 0
          ...     def __next__(self):
          ...         result = self.current
          ...         self.current += 2
          ...         return result
          ...     def __iter__(self):
          ...         return EvenNaturalsIterator()
          >>> evens = EvenNaturalsIterator()
          >>> even_iter1 = iter(evens)
          >>> even_iter2 = iter(evens)
          >>> next(even_iter1)
          4b569bf0e21d6369c5343767f1146f64
          # locked
          >>> next(even_iter1)
          805a87056a1a3fd559e4ef12a815b2be
          # locked
          >>> next(even_iter1)
          3cfd97a152be55d1a3486dbacb2bf637
          # locked
          >>> next(even_iter2)
          4b569bf0e21d6369c5343767f1146f64
          # locked
          >>> next(even_iter2)
          805a87056a1a3fd559e4ef12a815b2be
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
