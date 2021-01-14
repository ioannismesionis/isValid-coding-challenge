# Import packages
import pytest

# Import the function isValid() for testing
from main import isValid

@pytest.mark.parametrize('str_input, expected_output', [('abccc', 'No'), ('abbcc', 'No'), ('aabbbccc', 'No'), ('', 'No')])
def test_not_valid_strings(str_input, expected_output):
    """ Testing input strings that are not valid """
    actual_output = isValid(str_input)

    assert actual_output == expected_output, 'Actual{0}, Expected{1}'.format(actual_output, expected_output)


@pytest.mark.parametrize('str_input, expected_output', [('abc', 'Yes'), ('abcc', 'Yes'), ('aabbbcc', 'Yes'), ('a', 'Yes'), ('ab', 'Yes')])
def test_valid_strings(str_input, expected_output):
    """ Testing input strings that are valid """
    actual_output = isValid(str_input)

    assert actual_output == expected_output, 'Actual{0}, Expected{1}'.format(actual_output, expected_output)