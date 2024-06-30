from dataclasses import dataclass

@dataclass
class Locale:
    business_id:str
    full_address:str
    active:str
    categories:str
    city:str
    review_count:int
    business_name:str
    neighborhoods:str
    latitude:float
    longitude:float
    state:str
    stars:float
    mediaRecensioni: float


    def __hash__(self):
        return hash(self. business_id)

    def __str__(self):
        return f"{self. business_name}"