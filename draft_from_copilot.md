# ByteBites UML Class Diagram

+----------------+
|   Customer     |
+----------------+
| - name: str    |
| - history: list|
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
| - items: list  |
+----------------+
| + filter_by_category(category: str) -> list |
+----------------+

+----------------+
|     Order      |
+----------------+
| - items: list  |
+----------------+
| + compute_total() -> float |
+----------------+

# Relationships:
- Customer has a purchase history (list of Order objects).
- Menu holds a collection of MenuItem objects.
- Order contains a list of MenuItem