import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pytest
from unittest.mock import Mock
from bun import Bun
from ingredient import Ingredient


@pytest.fixture
def mock_bun():
    "Создает мок для булки"
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Флюоресцентная булка"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_ingredient():
    "Создает мок для ингредиента"
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "Соус"
    ingredient.get_price.return_value = 50.0
    ingredient.get_type.return_value = "sauce"
    return ingredient