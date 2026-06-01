import json
import os
from src.schemas import IndexModel, ProvinceModel


def test_index_validates():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'v1', 'index.json'))
    assert os.path.exists(path)
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # Will raise ValidationError if invalid
    IndexModel.model_validate(data)


def test_province_files_validate():
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'v1', 'provinsi'))
    assert os.path.isdir(base)
    files = [f for f in os.listdir(base) if f.endswith('.json')]
    assert files
    for fn in files[:5]:  # validate first 5 files as a smoke test
        path = os.path.join(base, fn)
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        ProvinceModel.model_validate(data)
