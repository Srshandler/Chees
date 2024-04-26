 from src.color import Color
from src.part import King
from src.part import King


def test_part_king_recalc_ex1():
  board = Board()
  part_w = King(Color.WHITE)
  part_b = King(Color.BLACK)
  board.put(0, 0, part_w)
  board.put(0, 1, part_b)
  part_w.recalc(board, 0, 0)
  assert len(part_w._positions) == 8

def test_part_rock_recalc_empty():
  board = Board()
  part = Rock(Color.WHITE)
  part.recalc(board, 0, 0)
  assert len(part._positions) == 14




def test_part_king_ctor_w():
  
  colors = [Color.WHITE, Color.BLACK]

  for c in colors:    
    part = King(c)
    assert part._mark_black == "♚"
    assert part._mark_white == "♔"
    assert part._color == c
    assert part._name == "King"
    assert part._positions == []