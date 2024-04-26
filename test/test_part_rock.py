from src.color import Color
from src.part import Rock

# pip install pytest

def test_part_rock_ctor_w():

  colors = [Color.WHITE, Color.BLACK]

  for c in colors:    
    part = Rock(c)
    assert part._mark_black == "♜"
    assert part._mark_white == "♖"
    assert part._color == c
    assert part._name == "Rock"
    assert part._positions == []
