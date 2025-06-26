import pytest
import functions.service as ser
import unittest.mock as mock
import requests


# Using unittest
@mock.patch("functions.service.get_user_from_db")
def test_get_user_from_db_with_mock(mock_get):
    # Configure the mock
    mock_get.return_value = 'Mocked Alice'
    
    # Call function
    result = ser.get_user_from_db(1)
    
    # Verify
    assert result == 'Mocked Alice'
    mock_get.assert_called_once_with(1)


# Using pytest-mock
def test_get_user_from_db_with_mock_two(mocker):
    fake_dict = mocker.patch('functions.service.get_user_from_db', return_value='Mocked Alice')
    assert ser.get_user_from_db(1) == 'Mocked Alice'
    fake_dict.assert_called_once_with(1)


# Using unittest for API testing
@mock.patch('requests.get')
def test_get_comments(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
    "id": 1,
    "postId": 1,
    "userId": 1,
    "comment": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut hendrerit ipsum ac velit sollicitudin, id fringilla sapien dapibus. Nulla condimentum ullamcorper tellus vel tristique. Donec nec sagittis ante. Proin semper, nunc et bibendum eleifend, odio justo facilisis nunc, vel ullamcorper tortor sapien at eros. Etiam euismod felis vel elit lobortis laoreet. Maecenas ac lobortis diam. Proin vitae neque sit amet ante pretium consectetur. Nulla facilisi."
  }
    mock_get.return_value = mock_response
    data = ser.get_comments()
    assert data == {
    "id": 1,
    "postId": 1,
    "userId": 1,
    "comment": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut hendrerit ipsum ac velit sollicitudin, id fringilla sapien dapibus. Nulla condimentum ullamcorper tellus vel tristique. Donec nec sagittis ante. Proin semper, nunc et bibendum eleifend, odio justo facilisis nunc, vel ullamcorper tortor sapien at eros. Etiam euismod felis vel elit lobortis laoreet. Maecenas ac lobortis diam. Proin vitae neque sit amet ante pretium consectetur. Nulla facilisi."
  }
    

@mock.patch('requests.get')
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.exceptions.HTTPError):
        ser.get_comments()