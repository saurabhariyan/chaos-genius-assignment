## Request Response API:
```BASE_URL/api/dimensions/ecommerce```

```
    [
    "UnitPrice",
    "Quantity",
    "PurchaseTime",
    "DayOfWeek"
    ]
```

```BASE_URL/api/tree/bank-marketing/job/?min-impact=0.128```

```      [
            {
                "avg_duration_impact": 0.129,
                "avg_duration_mean_g1": 4.639,
                "avg_duration_mean_g2": 4.752,
                "avg_duration_size_g1": 3.179,
                "avg_duration_size_g2": 5.825,
                "avg_duration_val_g1": 0.147,
                "avg_duration_val_g2": 0.277,
                "id": 6,
                "parent": {
                    "job": -1
                },
                "string": "job = housemaid"
            }
        ]
```
## steps to run locally:
        - create a virtualenv
        - `pip install requriments.txt`
        - `python manage.py runserver`


## Project Structure

    .
    ├── README.md
    ├── config
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── data
    │   ├── bank-marketing.json
    │   └── ecommerce.json
    ├── dataparser
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── admin.py
    │   ├── apps.py
    │   ├── consts.py
    │   ├── load_data.py
    │   ├── migrations
    │   ├── urls.py
    │   └── views.py
    ├── manage.py
    ├── requirements.txt
    └── system-design.md


## Production Ready
Documenting things skipped in the assignement that i would do in a real production web app,
some are kept for ease of demo and others for time constraint.

* Dockerize the app
* settings.debug = True
* settings has a public secret key.
* Add test cases
* Remove DRF browseable APIs
* Add caching based on bussiness logic, how quickly the files are updated, etc.


## Limitations:
both input files are stored locally in the data folder. updates *might* require a server restart.