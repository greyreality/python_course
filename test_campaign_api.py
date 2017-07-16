import requests
import json
from jsonschema import validate

api_url='http://sglzdstggo1.sgdc:5691'
schema={
    "type" : "object",
    "properties": {
        "auto_cache_is_ok": {
            "id": "/properties/auto_cache_is_ok",
            "type": "boolean"
        },
        "cache_is_ok": {
            "id": "/properties/cache_is_ok",
            "type": "boolean"
        },
        "db_is_ok": {
            "id": "/properties/db_is_ok",
            "type": "boolean"
        },
        "service": {
            "id": "/properties/service",
            "type": "string"
        },
        "status": {
            "id": "/properties/status",
            "type": "string"
        },
        "struct_cache_is_ok": {
            "id": "/properties/struct_cache_is_ok",
            "type": "boolean"
        },
        "venture": {
            "id": "/properties/venture",
            "type": "string"
        },
        "version": {
            "id": "/properties/version",
            "type": "string"
        }
    },
}

headers = dict(
    Accept='application/json'
)

def test_health_check_url():
    responce = requests.get(api_url+'/health_check')
    assert (responce.status_code == 200), 'Wrong responce =%s' % responce

def test_health_check_schema():
    responce = requests.get(url=api_url+'/health_check',params=headers).json()
    assert validate(responce,schema) == None

def test_rev():
    responce = requests.get(api_url+'/rev.txt')
    assert responce.status_code == 200