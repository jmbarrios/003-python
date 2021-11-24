import pytest
import homework


@pytest.mark.parametrize('test_input, expected',[
    ('https://www.inaturalist.org/observations/80657883', '80657883'),
    ('https://stackoverflow.com/questions/57823033', '57823033'),
    ('https://www.facebook.com/groups/ScienceMemes/posts/1110454509767273', '1110454509767273'),
    ('https://www.w3schools.com/43356356','43356356')
])
def test_obten_id(test_input, expected):
    assert (homework.obten_id(test_input) == expected or
            homework.obten_id(test_input) == int(expected))
