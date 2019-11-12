import random
import string


def randomStringDigits(stringLength=15):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

def getTokens(number_of_token = 5):
    token_list = []
    token = {}
    for itr in range(1, int(number_of_token)):
        token = { 'token': randomStringDigits(40), 'counter': 0, 'isAvailable': True,  'last_active_date_time': '', 'last_inactive_date_time': '' }
        token_list.append(token)
    return token_list
