

class Piece():
  """ Klasa będąca szkicem dla figur szachowych """

  def __init__(self, position: str):
    """ Inicjator pokazujący pozycję niesprecyzowanej figury """
    position = list(position)
    file = position[0]
    rank = int(position[1])

    if file in ["a", "b", "c", "d", "e", "f", "g", "h"] and rank in range(1,9):
      self.notation = [file, rank]
    else:
      print("Pole figury może znajdować się tylko w zakresie: wiersz (a-h), kolumna (1-8)")
      raise ValueError

  def check_move(self, notation: str):
    """ Metoda sprawdzająca czy ruch danej figury jest możliwy """
    pass

  def move(self, notation: str):
    """ Metoda wykonująca ruch figurą """
    pass

  def square(self):
    """ Metoda zwraca aktualną pozycję figury """
    return f"Pozycja figury: {self.notation}"

piece = Piece('g1')

class Pawn(Piece):
  """ Klasa reprezentująca pionka szachowego. Pochodna z klasy Piece """
  def __init__(self, position: str):
    super().__init__(position)

  def check_move_white(self, move: str):
    """ Metoda sprawdzająca czy dany ruch jest wykonywalny przez pionka """

    move = list(move)
    move[1] = int(move[1])

    # ta zmienna ma formę listy ["b", 1]
    # kod konwertujący literę kolumny na cyfrę:
    # dict_convertion = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
    # move[0] = dict_convertion[move[0]]

    if move[1] == self.notation[1] + 1 or move[1] == self.notation[1] + 2:
      return True
    else:
      return False

  def check_move_black(self, move: str):
    """ Metoda sprawdzająca czy dany ruch jest wykonywalny przez pionka """

    move = list(move)
    move[1] = int(move[1])

    # ta zmienna ma formę listy ["b", 1]
    # kod konwertujący literę kolumny na cyfrę:
    # dict_convertion = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
    # move[0] = dict_convertion[move[0]]

    if move[1] == self.notation[1] - 1 or move[1] == self.notation[1] - 2:
      return True
    else:
      return False


  def move_white(self, move: str):
    if self.check_move_white(move) == True:
      move = list(move)
      move[1] = int(move[1])
      self.notation = move
    else:
      raise ValueError("Ten ruch jest niedozwolony dla tej figury")

  def move_black(self, move: str):
    if self.check_move_black(move) == True:
      move = list(move)
      move[1] = int(move[1])
      self.notation = move
    else:
      raise ValueError("Ten ruch jest niedozwolony dla tej figury")

p1 = Pawn('a2')
print(p1.notation)
print(p1.check_move_white('a5'),\
      p1.check_move_white('a3'))
p1.move('a4')

class Chessboard():
  """ Klasa tworząca szachownicę """
  def __init__(self):
    self.reset()

  def reset(self):
    " Metoda ustawiająca pionki w pozycji wyjściowej"
    self.white_pawns = [Pawn("a2"), Pawn("b2"), Pawn("c2"), Pawn("d2"), Pawn ("e2"), Pawn("f2"), Pawn("g2"), Pawn("h2")]
    self.black_pawns = [Pawn("a7"), Pawn("b7"), Pawn("c7"), Pawn("d7"), Pawn ("e7"), Pawn("f7"), Pawn("g7"), Pawn("h7")]
    self.tura = 0

  def move(self, notation: str):
    " Metoda zmieniająca pozycję pionka "
    # zmienna sterująca tura = 0, to atrybut klasy Chessboard, który będzie stwierdzał, czy mają się poruszyć pionki białe (parzyste)\
    # czy czarne (nieparzyste).

    if self.tura % 2 == 0:
      for pawn in self.white_pawns:
        if pawn.notation[0] == list(notation)[0]:
          pawn.move_white(notation)
          print(pawn.notation)
          self.tura += 1

    else:
      for pawn in self.black_pawns:
        if pawn.notation[0] == list(notation)[0]:
          pawn.move_black(notation)
          print(pawn.notation)
          self.tura += 1





game = Chessboard()
game.move("b3") # White pawn moves from b2 to b3
game.move("f5") # Black pawn moves from f7 to f5
#game.move("g6")
# print(game.move("a4"))
