import json
import os
from src.fetch_normalize import parse_price, slugify


def test_parse_numeric_string():
    val, status = parse_price('12600')
    assert val == 12600
    assert status == 'available'


def test_parse_rupiah_format():
    val, status = parse_price('Rp 10.000')
    assert val == 10000
    assert status == 'available'


def test_parse_decimal_thousand():
    val, status = parse_price('Rp 6.800')
    assert val == 6800
    assert status == 'available'


def test_parse_zero_unavailable():
    val, status = parse_price('0')
    assert val is None
    assert status == 'unavailable'


def test_parse_none_unavailable():
    val, status = parse_price(None)
    assert val is None
    assert status == 'unavailable'


def test_slugify_examples():
    assert slugify('Prov. Aceh') == 'aceh'
    assert slugify('Prov. DI Yogyakarta') == 'di-yogyakarta'
    assert slugify('Free Trade Zone (FTZ) Sabang') == 'free-trade-zone-ftz-sabang'


def test_generated_index_exists():
    path = os.path.join(os.path.dirname(__file__), '..', 'v1', 'index.json')
    path = os.path.abspath(path)
    assert os.path.exists(path)
    with open(path, 'r', encoding='utf-8') as f:
        idx = json.load(f)
    assert 'provinsi_count' in idx
    assert idx['provinsi_count'] >= 0
