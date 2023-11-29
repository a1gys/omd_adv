import keyword as kw
from typing import Dict


class JsonHandler:
    """
    Sets all keys with values in json file iteratively
    """
    def __init__(self, json_data: Dict):
        for key, value in json_data.items():
            if isinstance(value, dict):
                setattr(self, key, JsonHandler(value))
            else:
                setattr(self, key + "_", value) if kw.iskeyword(key) \
                    else setattr(self, key, value)


class ColorizeMixin:
    repr_color_code = 37  # white
    bg_color_code = 40  # black

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "__repr__"):
            raise TypeError(f"{cls.__name__} must implement either __str__ or\
                             __repr__ method")

    def color_repr(self, text: str):
        return f"\033[1;{self.repr_color_code};{self.bg_color_code}m{text}"


class Advert(ColorizeMixin, JsonHandler):
    repr_color_code = 32  # green
    bg_color_code = 40  # black

    def __init__(self, json_data: Dict):
        if "title" not in json_data:
            raise ValueError("attribute 'title' is mandatory")
        super().__init__(json_data)

    @property
    def price(self):
        return getattr(self, "price_", 0) if hasattr(self, "price_") else 0

    @price.setter
    def price(self, value):
        if value >= 0:
            setattr(self, "price_", value)
        else:
            raise ValueError("must be >= 0")

    def __repr__(self):
        return self.color_repr(text=f"{self.title} | {self.price} ₽")
