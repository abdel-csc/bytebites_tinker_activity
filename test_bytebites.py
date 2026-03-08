from models import Customer, MenuItem, Menu, Order


def test_order_total_with_multiple_items():
    order = Order()
    order.items = [
        MenuItem('Spicy Burger', 10.99, 'Food', 5),
        MenuItem('Large Soda', 2.99, 'Drinks', 3)
    ]
    assert order.compute_total() == 13.98


def test_order_total_is_zero_when_empty():
    order = Order()
    assert order.compute_total() == 0


def test_filter_by_category():
    menu = Menu()
    menu.items = [
        MenuItem('Large Soda', 2.99, 'Drinks', 3),
        MenuItem('Spicy Burger', 10.99, 'Food', 5)
    ]
    results = menu.filter_by_category('Drinks')
    assert len(results) == 1
    assert results[0].name == 'Large Soda'
