GETTING STARTED
===============

# Installation

<b>The repository does not support windows according to Django-Oscar documentation.</b>

* Create Virtual Environment

```
$ python -m venv .venv
$ source .venv/bin/activate # For linux
```


* Install packages

```
$ pip install -r requirements.txt
```

# Populate data

* Populate Countries

```
$ pip install pycountry
$ python manage.py oscar_populate_countries --no-shipping
```
        
* Every Oscar deployment needs at least one product class and one fulfilment partner. These aren’t created automatically.

 