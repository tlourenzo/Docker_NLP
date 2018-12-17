"""Module containing all response codes available in the API."""

error = {
  'Unauthorized': [401, 'Wrong login details!'],
  'Payment_Required': [402, ''],
  'Unsupported_Media_Type': [415, ''],
  'Unknown_User': [406, 'Please register before login!'],
  'Existing_User': [405, 'User already registered!']
}


success = {
    'Created': [201, 'User successfully created'],
    'Authorized': [202, 'Login accepted,  Tokens available: '],
    'Password_Changed': [203, 'Password changed successfully']
}
