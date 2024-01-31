GETTING STARTED
===============

<b>According to Django-Oscar documentation, the repository does not support Windows OS.</b>

# Installation


* Create Virtual Environment

    ```
    python -m venv .venv
    ```

* Activate Environment

    ```
    source .venv/bin/activate
    ```


* Install packages

    ```
    pip install -r requirements.txt
    ```

# Migrate Database

```
python manage.py migrate
```

# Populate data

* Install package

    ```
    pip install pycountry
    ```

* Populate countries.
    
    Omit <code>--no-shipping</code> to enable shipping for all countries.

    ```
    python manage.py oscar_populate_countries --no-shipping
    ```
        
* Every Oscar deployment needs at least one product class and one fulfilment partner. These aren’t created automatically.

* Create an Admin account
    
    ```
    python manage.py createsuperuser
    ```