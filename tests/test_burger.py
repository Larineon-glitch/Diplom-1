import pytest
from unittest.mock import Mock, patch
from burger import Burger
from ingredient import Ingredient
from bun import Bun


class TestBurger:
    
    @pytest.fixture
    def burger(self):
        return Burger()
    
    def test_set_buns(self, burger, mock_bun):
        "Тест установки булки"
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
    
    def test_add_ingredient(self, burger, mock_ingredient):
        "Тест добавления ингредиента"
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient
    
    def test_remove_ingredient(self, burger, mock_ingredient):
        "Тест удаления ингредиента"
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0
    
    def test_move_ingredient(self, burger, mock_ingredient):
        "Тест перемещения ингредиента"
        ingredient2 = Mock(spec=Ingredient)
        ingredient2.get_name.return_value = "Сыр"
        
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(ingredient2)
        
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_ingredient
        assert burger.ingredients[0] == ingredient2
    
    def test_get_price_with_ingredients(self, burger, mock_bun, mock_ingredient):
        "Тест расчета стоимости с ингредиентами"
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        
        expected_price = 100.0 * 2 + 50.0 * 2
        assert burger.get_price() == expected_price
    
    def test_get_price_without_ingredients(self, burger, mock_bun):
        "Тест расчета стоимости без ингредиентов"
        burger.set_buns(mock_bun)
        expected_price = 100.0 * 2
        assert burger.get_price() == expected_price
    
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    def test_get_receipt(self, mock_ingredient_class, mock_bun_class, burger):
        "Тест получения чека"
        # Создаем мок для булки
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Булка"
        mock_bun.get_price.return_value = 50.0
        mock_bun_class.return_value = mock_bun
        
        # Создаем моки для ингредиентов
        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = "Кетчуп"
        mock_ingredient1.get_price.return_value = 30.0
        mock_ingredient1.get_type.return_value = "sauce"
        
        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = "Сыр"
        mock_ingredient2.get_price.return_value = 40.0
        mock_ingredient2.get_type.return_value = "filling"
        
        mock_ingredient_class.side_effect = [mock_ingredient1, mock_ingredient2]
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        
        receipt = burger.get_receipt()
        
        assert "Булка" in receipt
        assert "Кетчуп" in receipt
        assert "Сыр" in receipt
        assert "170" in receipt or "170.0" in receipt
    
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    def test_get_receipt_without_ingredients(self, mock_ingredient_class, mock_bun_class, burger):
        "Тест получения чека без ингредиентов"
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Булка"
        mock_bun.get_price.return_value = 50.0
        mock_bun_class.return_value = mock_bun
        
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        
        assert "Булка" in receipt
        assert "100" in receipt or "100.0" in receipt
    
    def test_ingredient_count(self, burger, mock_ingredient):
        "Тест подсчета ингредиентов"
        assert burger.get_ingredient_count() == 0
        
        burger.add_ingredient(mock_ingredient)
        assert burger.get_ingredient_count() == 1
        
        burger.add_ingredient(mock_ingredient)
        assert burger.get_ingredient_count() == 2
    
    @pytest.mark.parametrize("ingredient_type,expected_type", [
        ("sauce", "sauce"),
        ("filling", "filling"),
        ("bun", "bun"),
    ])
    def test_ingredient_types(self, ingredient_type, expected_type, burger):
        "Параметризованный тест для разных типов ингредиентов"
        mock_ing = Mock(spec=Ingredient)
        mock_ing.get_type.return_value = ingredient_type
        burger.add_ingredient(mock_ing)
        assert burger.ingredients[0].get_type() == expected_type
    
    def test_remove_ingredient_index_error(self, burger):
        "Тест удаления ингредиента с несуществующим индексом"
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)
    
    def test_move_ingredient_index_error(self, burger):
        "Тест перемещения ингредиента с несуществующим индексом"
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 1)