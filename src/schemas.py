from __future__ import annotations
from typing import List, Optional, Literal
from pydantic import BaseModel, Field, ValidationError, constr


Availability = Literal['available', 'unavailable', 'unknown']


class ProductModel(BaseModel):
    product: constr(strip_whitespace=True)
    product_canonical: Optional[constr(strip_whitespace=True)] = None
    price_rupiah: Optional[int] = None
    availability: Availability
    pertamina_updated_at: Optional[str] = None


class ProvinceModel(BaseModel):
    province: constr(strip_whitespace=True)
    province_slug: constr(strip_whitespace=True)
    pertamina_updated_at: Optional[str] = None
    synced_at: constr(strip_whitespace=True)
    products: List[ProductModel]


class IndexProvinceEntry(BaseModel):
    name: constr(strip_whitespace=True)
    slug: constr(strip_whitespace=True)
    path: constr(strip_whitespace=True)
    pertamina_updated_at: Optional[str] = None
    synced_at: constr(strip_whitespace=True)
    products_count: int
    file_size_bytes: int


class IndexModel(BaseModel):
    api_name: constr(strip_whitespace=True)
    version: constr(strip_whitespace=True)
    author: constr(strip_whitespace=True)
    github_repository: constr(strip_whitespace=True)
    synced_at: constr(strip_whitespace=True)
    pertamina_updated_at: Optional[str] = None
    provinsi_count: int
    provinsi: dict[str, IndexProvinceEntry]
    endpoints: dict
    notes: Optional[str] = None
