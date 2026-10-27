import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from main import *


def test_sumar():
    assert sumar(4, 9) == 13
    assert sumar(10, 5) == 15


def test_restar():
    assert restar(10, 5) == 5
    assert restar(20, 10) == 10


def test_multiplicar():
    assert multiplicar(4, 5) == 20
    assert multiplicar(3, 7) == 21


def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(15, 3) == 5
