# Installation

- Install requirements.txt on your virtual enviroment.
```bash
pip install -r requirements.txt
```

- Load parking.json to database.
```bash
python manage.py loaddata parking.json
```

## API
There are totally 3 endpoints

- Parking (POST)

http://127.0.0.1:8000/api/parking/

- Unparking (POST)

http://127.0.0.1:8000/api/unparking/

-Parking Information (GET)

http://127.0.0.1:8000/api/parking-info/

