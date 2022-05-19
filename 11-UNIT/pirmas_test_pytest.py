import pytest
from personal_code import PersonalCode


def test_last_4_personal_code():
    test_code = "33309240063"
    kodas = PersonalCode(test_code)
    assert kodas.return_last_four() == test_code[-4:]

retcode = pytest.main(["pirmas_test_pytest.py"])