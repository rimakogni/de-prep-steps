"""
Write a function that takes a string (name) and a number (year_of_birth) and returns an object with:

 - a name property set to the value of the name parameter
 - an age property set to whatever the age of the northcoder would be in the year 2023
 - a language property set to 'Python'

If the year is after 2023, show 'error' for the age.
 
create_northcoder('Joe', 2002) 

returns 
{ 
  'name': 'Joe', 
  'age': 21, 
  'language': 'Python' 
} 
"""

def create_northcoder(name, year_of_birth):
    # Your code here
    pass


def test_creates_northcoder_with_correct_age():
    result = create_northcoder('Joe', 2002)
    expected = { 
                'name': 'Joe', 
                'age': 21, 
                'language': 'Python' 
               } 
    assert result == expected


def test_2023_baby_is_0_years_old():
    result = create_northcoder('Paul', 2023)
    expected = { 
                'name': 'Paul', 
                'age': 0, 
                'language': 'Python' 
               } 
    assert result == expected


def test_2123_baby_shows_age_error():
    result = create_northcoder('Zarkon', 2123)
    expected = { 
                'name': 'Zarkon', 
                'age': 'error', 
                'language': 'Python' 
               } 
    assert result == expected