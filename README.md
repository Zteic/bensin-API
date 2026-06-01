# Bensin-API (static generator)

This repository contains a simple generator that normalizes Pertamina price payloads into static JSON files suitable for public consumption.

Quick start (on Windows, with `.venv` activated):

1. Install dependencies (if you want optional validation/fetch features):

```powershell
# using uv as pip replacement, per your setup
uv install -r requirements.txt
```

2. Run the generator (reads `price.json` and writes `v1/` files):

```powershell
python src\fetch_normalize.py
```

Outputs:

- `v1/index.json` - metadata and endpoints
- `v1/nasional.json` - list of provinces and quick metadata
- `v1/provinsi/{slug}.json` - per-province normalized price data# bensin-api
  API untuk cek harga bensin dari Pertamina, diurutkan berdasarkan tiap provinsi.
