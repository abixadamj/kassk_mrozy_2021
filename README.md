# kassk_mrozy_2021
Przykład fastAPI na warsztaty Kassk &amp; Mrozy 2021

## Przykładowe wywołania:

* http://office.abixedukacja.eu:5000/welcome?user=%22Adam%22
* http://office.abixedukacja.eu:5000/welcome/?user=adasiek&welcome=tt
* http://office.abixedukacja.eu:5000/welcome-json/adam
* http://office.abixedukacja.eu:5000/welcome-json/adam?welcome=uuu
* http://office.abixedukacja.eu:5000/auth

Serwer:
* http://office.abixedukacja.eu:5000/
* Na nim pokażemy `tail -f /tmp/kassk_mrozy_2021.log `

----
Przykład połączenia z IDLE:
```
import requests
r = requests.get("http://office.abixedukacja.eu:5000/welcome/?user=Adasiek")
r.content
r = requests.get("http://office.abixedukacja.eu:5000/welcome-json/adam")
r.content
r.json()
```

Dużo więcej na stronie: https://docs.python-requests.org/en/master/user/quickstart/

----

Materiały z projektu Koduj z klasą (rok 2014) - mogą wymagać aktualizacji kodów:

* https://python101.readthedocs.io/pl/latest/
* https://github.com/koduj-z-klasa/python101