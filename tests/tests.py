from main import Rostelecom
from settings import valid_telephone_7, valid_email, valid_login, valid_personal_account, valid_password, invalid_password, \
    valid_telephone_8, invalid_telephone_1, invalid_telephone_2, invalid_telephone_3, \
    valid_email_1, invalid_email_2, invalid_email_3, invalid_email_4, invalid_personal_account_4, \
    invalid_personal_account_6, invalid_personal_account_8, invalid_personal_account_11

import os

pf = Rostelecom()


# ts-001
def test_get_api_key_with_correct_telephone_7_and_correct_password(telephone_7=valid_telephone_7, password=valid_password):
    """Проверка авторизации существующего клиента по номеру мобильного телефона и паролю,
    с использованием корректных данных и кода абонента "7"."""
    status, result = pf.get_api_key_tel7(telephone_7, password)

    assert status == 200
    assert 'key' in result

# ts-002
def test_get_api_key_with_correct_email_and_correct_password(email=valid_email, password=valid_password):
    """Проверка авторизации существующего клиента по почте и паролю, с использованием корректных данных."""
    status, result = pf.get_api_key_mail(email, password)

    assert status == 200
    assert 'key' in result

# ts-003
def test_get_api_key_with_correct_login_and_correct_password(login=valid_login, password=valid_password):
    """Проверка авторизации существующего клиента по логину и паролю, с использованием корректных данных."""
    status, result = pf.get_api_key_log(login, password)

    assert status == 200
    assert 'key' in result

# ts-004
def test_get_api_key_with_correct_personal_account_and_correct_password(personal_account=valid_personal_account, password=valid_password):
    """Проверка авторизации существующего клиента по лицевому счёту и паролю, с использованием корректных данных."""
    status, result = pf.get_api_key_account(personal_account, password)

    assert status == 200
    assert 'key' in result

# ts-005
def test_get_api_key_with_correct_telephone_8_and_correct_password(telephone_8=valid_telephone_8, password=valid_password):
    """Проверка авторизации существующего клиента по номеру мобильного телефона и паролю,
    с использованием корректных данных и кода абонента "8"."""
    status, result = pf.get_api_key_tel8(telephone_8, password)

    assert status == 200
    assert 'key' in result

# ts-006
def test_get_api_key_with_wrong_telephone_1_and_correct_password(telephone_1=invalid_telephone_1, password=valid_password):
    """Проверка авторизации с использованием некорректного телефону 12 цифр и корректного пароля."""
    status, result = pf.get_api_key_tel1(telephone_1, password)

    assert status == 403
    assert 'key' in result

# ts-007
def test_get_api_key_with_wrong_telephone_2_and_correct_password(telephone_2=invalid_telephone_2, password=valid_password):
    """Проверка авторизации с использованием некорректного телефона 10 цифр и корректного пароля."""
    status, result = pf.get_api_key_tel2(telephone_2, password)

    assert status == 403
    assert 'key' in result

# ts-008
def test_get_api_key_with_wrong_telephone_3_and_correct_password(telephone_3=invalid_telephone_3, password=valid_password):
    """Проверка авторизации с использованием некорректного телефона 10 цифр, 1 буква и корректного пароля."""
    status, result = pf.get_api_key_tel3(telephone_3, password)

    assert status == 403
    assert 'key' in result


# ts-009
def test_get_api_key_with_invalid_personal_account_4_and_correct_password(personal_account_4=invalid_personal_account_4, password=valid_password):
    """Проверка авторизации по не валидному лицевому счёту (4 цифры) и корректному паролю."""
    """Номер лицевого счёта - 5-7 цифр для Москвы и 12 цифр для других регионов из Договора на оказание услуг связи"""
    status, result = pf.get_api_key_account4(personal_account_4, password)

    assert status == 403
    assert 'key' in result

# ts-010
def test_get_api_key_with_invalid_personal_account_6_and_correct_password(personal_account_6=invalid_personal_account_6, password=valid_password):
    """Проверка авторизации по не валидному лицевому счёту (6 цифр) и корректному паролю."""
    """Номер лицевого счёта - 5-7 цифр для Москвы и 12 цифр для других регионов из Договора на оказание услуг связи"""
    status, result = pf.get_api_key_account6(personal_account_6, password)

    assert status == 403
    assert 'key' in result

# ts-011
def test_get_api_key_with_invalid_personal_account_8_and_correct_password(personal_account_8=invalid_personal_account_8, password=valid_password):
    """Проверка авторизации по не валидному лицевому счёту (8 цифры) и корректному паролю."""
    """Номер лицевого счёта - 5-7 цифр для Москвы и 12 цифр для других регионов из Договора на оказание услуг связи"""
    status, result = pf.get_api_key_account8(personal_account_8, password)

    assert status == 403
    assert 'key' in result

# ts-012
def test_get_api_key_with_invalid_personal_account_11_and_correct_password(personal_account_11=invalid_personal_account_11, password=valid_password):
    """Проверка авторизации по не валидному лицевому счёту (11 цифры) и корректному паролю."""
    """Номер лицевого счёта - 5-7 цифр для Москвы и 12 цифр для других регионов из Договора на оказание услуг связи"""
    status, result = pf.get_api_key_account11(personal_account_11, password)

    assert status == 403
    assert 'key' in result


# ts-013
def test_get_api_key_with_correct_telephone_7_and_wrong_password(telephone_7=valid_telephone_7, password=invalid_password):
    """Проверка авторизации существующего клиента с использованием корректного мобильного телефона и неверного пароля."""
    status, result = pf.get_api_key_tel7(telephone_7, password)

    assert status == 403
    assert 'key' in result

# ts-014
def test_get_api_key_with_correct_email_and_wrong_password(email=valid_email, password=invalid_password):
    """Проверка авторизации существующего клиента с использованием корректной почты и неверного пароля."""
    status, result = pf.get_api_key_mail(email, password)

    assert status == 403
    assert 'key' in result

# ts-015
def test_get_api_key_with_correct_login_and_wrong_password(login=valid_login, password=invalid_password):
    """Проверка авторизации существующего клиента с использованием корректного логина и неверного пароля."""
    status, result = pf.get_api_key_log(login, password)

    assert status == 403
    assert 'key' in result

# ts-016
def test_get_api_key_with_correct_personal_account_and_wrong_password(personal_account=valid_personal_account, password=invalid_password):
    """Проверка авторизации существующего клиента с использованием корректного лицевого счёта и неверного пароля."""
    status, result = pf.get_api_key_account(personal_account, password)

    assert status == 403
    assert 'key' in result
