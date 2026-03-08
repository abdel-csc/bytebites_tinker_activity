
+----------------+
|   Customer     |
+----------------+
| - name: str    |
| - history: list[Order] |
+----------------+

+----------------+
|   MenuItem     |
+----------------+
| - name: str    |
| - price: float |
| - category: str|
| - popularity: int |
+----------------+

+----------------+
|     Menu       |
+----------------+
| - items: list[MenuItem] |
+----------------+
| + filter_by_category(category: str) -> list[MenuItem] |
+----------------+

+----------------+
|     Order      |
+----------------+
| - items: list[MenuItem] |
+----------------+
| + compute_total() -> float |
+----------------+

# Relationships:
- Customer has a purchase history (list of Order objects).
- Menu holds a collection of MenuItem objects.
- Order contains a list of MenuItem objects.