import itertools
import random 
import string

password_options = string.ascii_lowercase+string.ascii_uppercase+string.punctuation+string.digits

password_length = 6
password = "".join(random.sample(password_options, password_length))

print("Password: "+password)


def guess_password(real):
    """Allows the guessing of passwords

    :param real: The actual password
    :type real: String
    :return: The password which has been found and in how many iterations
    :rtype: String
    """
    chars = password_options
    attempts = 0
    for pl in range(1, password_length+1):
        for guess in itertools.product(chars, repeat=pl):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return 'password is %s. found in %s guesses.' % (guess, attempts)
            
print(guess_password(password))