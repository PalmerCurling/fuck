#!/usr/bin/python

import requests
import getpass

#points to our URLS & establishes dictionary instance with current username
new_fucks = "http://murmuring-forest-5562.herokuapp.com/new_fucks"
number_fucks = "http://murmuring-forest-5562.herokuapp.com/number_fucks"
name = {"name": getpass.getuser()}


response = requests.post(new_fucks, data=name)
print response.text

#
#if :
#	r = requests.get(number_fucks)
#	print '{number} fucks given.'.format(number=r.text)
#else:
#	val = requests.post(new_fucks, data=name)
#	print val.text
