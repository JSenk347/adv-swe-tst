import pytest
from quote import build_quote
def make_line(quantity, stock=0):
    return{
                "id": 1,
                "name": "Jordans hammer",
                "stock": stock,
                "quantity": quantity,
                }

def test_stock_less_than_quantity():
    lines = [make_line(quantity=5)] 
    with pytest.raises(ValueError, match ="only 0 of Jordans hammer in stock"):
        build_quote(lines)

