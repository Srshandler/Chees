from src.color import Color
from src.part import Knight

def test_part_knight_ctor_w(): 
    
    colors = [Color.WHITE, Color.BLACK]
    
    for c in colors:    
        part = Knight(c)
        assert part._mark_black == "♞"
        assert part._mark_white == "♘"
        assert part._color == c
        assert part._name == "Knight"
        # assert part._positions == []
