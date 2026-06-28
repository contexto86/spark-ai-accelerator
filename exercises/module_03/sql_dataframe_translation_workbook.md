# SQL ↔ DataFrame Translation Workbook

## Query 01

```sql
SELECT municipality_id, municipality_name, canton FROM municipalities;
```

Prompts:

1. What does it do?
2. What physical plan shape do you expect?
3. Write the PySpark DataFrame equivalent.
4. Which version is more readable here?
5. When would SQL be preferable?
6. When would DataFrames be preferable?

## Query 02

```sql
SELECT * FROM transactions WHERE sale_price >= 750000;
```

Prompts:

1. What does it do?
2. What physical plan shape do you expect?
3. Write the PySpark DataFrame equivalent.
4. Which version is more readable here?
5. When would SQL be preferable?
6. When would DataFrames be preferable?

## Query 03

```sql
SELECT property_type, COUNT(*) AS transactions FROM transactions GROUP BY property_type;
```

Prompts:

1. What does it do?
2. What physical plan shape do you expect?
3. Write the PySpark DataFrame equivalent.
4. Which version is more readable here?
5. When would SQL be preferable?
6. When would DataFrames be preferable?

## Query 04

```sql
SELECT municipality_id, AVG(sale_price) AS avg_sale_price FROM transactions GROUP BY municipality_id;
```

Prompts:

1. What does it do?
2. What physical plan shape do you expect?
3. Write the PySpark DataFrame equivalent.
4. Which version is more readable here?
5. When would SQL be preferable?
6. When would DataFrames be preferable?

## Query 05

```sql
SELECT * FROM transactions ORDER BY sale_price DESC LIMIT 10;
```

Prompts:

1. What does it do?
2. What physical plan shape do you expect?
3. Write the PySpark DataFrame equivalent.
4. Which version is more readable here?
5. When would SQL be preferable?
6. When would DataFrames be preferable?

## Query 06

```sql
SELECT m.canton, COUNT(*) FROM municipalities m GROUP BY m.canton;
```

Prompts:

1. What does it do?
2. What physical plan shape do you expect?
3. Write the PySpark DataFrame equivalent.
4. Which version is more readable here?
5. When would SQL be preferable?
6. When would DataFrames be preferable?

## Query 07

```sql
SELECT t.*, m.canton FROM transactions t JOIN municipalities m ON t.municipality_id = m.municipality_id;
```

Prompts:

1. What does it do?
2. What physical plan shape do you expect?
3. Write the PySpark DataFrame equivalent.
4. Which version is more readable here?
5. When would SQL be preferable?
6. When would DataFrames be preferable?

## Query 08

```sql
SELECT m.canton, AVG(t.sale_price) FROM transactions t JOIN municipalities m ON t.municipality_id = m.municipality_id GROUP BY m.canton;
```

Prompts:

1. What does it do?
2. What physical plan shape do you expect?
3. Write the PySpark DataFrame equivalent.
4. Which version is more readable here?
5. When would SQL be preferable?
6. When would DataFrames be preferable?

## Query 09

```sql
SELECT property_type, MAX(sale_price) FROM transactions GROUP BY property_type;
```

Prompts:

1. What does it do?
2. What physical plan shape do you expect?
3. Write the PySpark DataFrame equivalent.
4. Which version is more readable here?
5. When would SQL be preferable?
6. When would DataFrames be preferable?

## Query 10

```sql
SELECT municipality_id, COUNT(DISTINCT property_id) FROM transactions GROUP BY municipality_id;
```

Prompts:

1. What does it do?
2. What physical plan shape do you expect?
3. Write the PySpark DataFrame equivalent.
4. Which version is more readable here?
5. When would SQL be preferable?
6. When would DataFrames be preferable?

## Query 11

```sql
SELECT * FROM population_history WHERE year = 2025;
```

Prompts:

1. What does it do?
2. What physical plan shape do you expect?
3. Write the PySpark DataFrame equivalent.
4. Which version is more readable here?
5. When would SQL be preferable?
6. When would DataFrames be preferable?

## Query 12

```sql
SELECT municipality_id, population FROM population_history WHERE year = 2025 AND population > 100000;
```

Prompts:

1. What does it do?
2. What physical plan shape do you expect?
3. Write the PySpark DataFrame equivalent.
4. Which version is more readable here?
5. When would SQL be preferable?
6. When would DataFrames be preferable?

## Query 13

```sql
SELECT transaction_id, sale_price, sale_price / 1000000.0 AS sale_price_millions FROM transactions;
```

Prompts:

1. What does it do?
2. What physical plan shape do you expect?
3. Write the PySpark DataFrame equivalent.
4. Which version is more readable here?
5. When would SQL be preferable?
6. When would DataFrames be preferable?

## Query 14

```sql
SELECT transaction_id, CASE WHEN sale_price >= 1000000 THEN 'premium' ELSE 'standard' END AS price_band FROM transactions;
```

Prompts:

1. What does it do?
2. What physical plan shape do you expect?
3. Write the PySpark DataFrame equivalent.
4. Which version is more readable here?
5. When would SQL be preferable?
6. When would DataFrames be preferable?

## Query 15

```sql
SELECT municipality_id, year, population, LAG(population) OVER (PARTITION BY municipality_id ORDER BY year) AS prev_population FROM population_history;
```

Prompts:

1. What does it do?
2. What physical plan shape do you expect?
3. Write the PySpark DataFrame equivalent.
4. Which version is more readable here?
5. When would SQL be preferable?
6. When would DataFrames be preferable?

## Query 16

```sql
SELECT municipality_id, year, population, population - LAG(population) OVER (PARTITION BY municipality_id ORDER BY year) AS population_change FROM population_history;
```

Prompts:

1. What does it do?
2. What physical plan shape do you expect?
3. Write the PySpark DataFrame equivalent.
4. Which version is more readable here?
5. When would SQL be preferable?
6. When would DataFrames be preferable?

## Query 17

```sql
SELECT * FROM (SELECT t.*, ROW_NUMBER() OVER (PARTITION BY municipality_id ORDER BY sale_price DESC, transaction_id ASC) AS rn FROM transactions t) x WHERE rn <= 2;
```

Prompts:

1. What does it do?
2. What physical plan shape do you expect?
3. Write the PySpark DataFrame equivalent.
4. Which version is more readable here?
5. When would SQL be preferable?
6. When would DataFrames be preferable?

## Query 18

```sql
SELECT m.canton, p.property_value_index FROM municipalities m JOIN property_values p ON m.municipality_id = p.municipality_id ORDER BY p.property_value_index DESC;
```

Prompts:

1. What does it do?
2. What physical plan shape do you expect?
3. Write the PySpark DataFrame equivalent.
4. Which version is more readable here?
5. When would SQL be preferable?
6. When would DataFrames be preferable?

## Query 19

```sql
SELECT m.canton, t.property_type, AVG(t.sale_price) AS avg_price FROM transactions t JOIN municipalities m ON t.municipality_id = m.municipality_id GROUP BY m.canton, t.property_type;
```

Prompts:

1. What does it do?
2. What physical plan shape do you expect?
3. Write the PySpark DataFrame equivalent.
4. Which version is more readable here?
5. When would SQL be preferable?
6. When would DataFrames be preferable?

## Query 20

```sql
SELECT m.canton, COUNT(*) AS txns, AVG(t.sale_price) AS avg_price FROM transactions t JOIN municipalities m ON t.municipality_id = m.municipality_id GROUP BY m.canton HAVING COUNT(*) >= 5 ORDER BY avg_price DESC;
```

Prompts:

1. What does it do?
2. What physical plan shape do you expect?
3. Write the PySpark DataFrame equivalent.
4. Which version is more readable here?
5. When would SQL be preferable?
6. When would DataFrames be preferable?
