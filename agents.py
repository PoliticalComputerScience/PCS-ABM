import mesa
from typing import List, Optional

class Household(mesa.Agent):
    def __init__(
        self,
        uid: int,
        model: mesa.Model,

        # Parameters
        wealth: int,
        income: int,
        my_rent: int,
        my_mortgage: int,
        
        rents_paid: List[House],
        houses_owned: List[House]
    ):
        super().__init__(uid, model)        
        self.wealth = wealth
        self.income = income
        self.my_rent = my_rent
        self.my_mortgage = my_mortgage


class House(mesa.Agent):
    def __init__(
        self,
        uid: int,
        model: mesa.Model,

        # Parameters
        price_to_buy: int,
        price_to_rent: int,
        owned_by: Optional[Household],
        rented_to: Optional[Household],
    ):
        super().__init__(uid, model)
        self.price_to_buy = price_to_buy
        self.price_to_rent = price_to_rent