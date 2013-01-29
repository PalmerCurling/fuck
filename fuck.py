import requests
import getpass

new_fuck="http://127.0.0.1:5000/new_fuck"
number_fucks= "http://127.0.0.1:5000/number_fucks"
name= {"name": getpass.getuser()}

requests.post(new_fuck, data=name)

r = requests.get(number_fucks)
print '{number} fucks given.'.format(number=r.text)
