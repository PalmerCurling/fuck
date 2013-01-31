import requests

fucks_given = "http://127.0.0.1:5000/"


r = requests.get (fucks_given)
print 'fucks recently given by: {fucks}'.format(fucks=r.text)

