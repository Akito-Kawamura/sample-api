import pytest
import json

def test_json():
	json_open = open('../json_mock/user.json', 'r')
	json_load = json.load(json_open)

	print(json_load)