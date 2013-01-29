import requests
import getpass

#points to our URLS & establishes dictionary instance with current username
new_fucks = "http://127.0.0.1:5000/new_fucks"
number_fucks = "http://127.0.0.1:5000/number_fucks"
name = {"name": getpass.getuser()}

#gives a fuck to the server
requests.post(new_fucks, data=name)

#returns fucks given, according to server
r = requests.get(number_fucks)
print '{number} fucks given.'.format(number=r.text)
