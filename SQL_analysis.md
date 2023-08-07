## Analysis using SQL

#### Task 1 How many values are there in the given dataset?

<pre>
SELECT COUNT(*)
FROM ecommerce
</pre>

#### Task 2 Find out the unique brands in the given dataset

<pre>
SELECT DISTINCT brand
FROM ecommerce
</pre>

#### Task 3 Retrieve all records from the 'ecommerce' table where the brand is 'Amazon'.

<pre>
SELECT *
FROM ecommerce
WHERE brand = "Amazon"
</pre>

#### Task 4 Retrieve all records from the 'ecommerce' table where the product reviews contain the word 'good' in their text.

<pre>
SELECT *
FROM ecommerce
WHERE reviews_text LIKE "%good%"
</pre>

#### Task 5 Provide a list of all products and their corresponding details from the 'ecommerce' table that belong to the 'Electronics' category

<pre>
SELECT *
FROM ecommerce
WHERE categories LIKE '%Electronics%'
</pre>

#### Task 6 Retrieve all records from the 'ecommerce' table where the products are categorized under 'Electronics' as their primary category and the brand is 'Flipkart'.

<pre>
SELECT *
FROM ecommerce
WHERE brand = 'Flipkart'
AND primaryCategories = 'Electronics'
</pre>

#### Task 7 Provide a summary of the number of positive and negative sentiments for each primary category in the 'ecommerce' table.

<pre>
SELECT primaryCategories,
  SUM(CASE
    WHEN sentiment = 'positive' THEN 1
    ELSE 0
  END) AS positive_count,
  SUM(CASE
    WHEN sentiment = 'negative' THEN 1
    ELSE 0
  END) AS negative_count
FROM ecommerce
GROUP BY primaryCategories;
</pre>

#### Task 8 Retrieve all records from the 'ecommerce' table where the sentiment in the product reviews is classified as 'positive'.

<pre>
SELECT *
FROM ecommerce
WHERE sentiment = 'positive'
</pre>

#### Task 9 Provide a summary report for each brand in the 'ecommerce' table, including the total number of positive and negative sentiments in product reviews, the total number of reviews, and the percentage of positive and negative sentiments for each brand.

<pre>
SELECT brand,
  COUNT(*) AS total_reviews,
  SUM(CASE
    WHEN sentiment = 'positive' THEN 1
    ELSE 0
  END) AS positive_count,
  SUM(CASE
    WHEN sentiment = 'negative' THEN 1
    ELSE 0
  END) AS negative_count,
  ROUND(SUM(CASE
    WHEN sentiment = 'positive' THEN 1
    ELSE 0
  END) * 100.0 / COUNT(*), 2) AS positive_percentage,
  ROUND(SUM(CASE
    WHEN sentiment = 'negative' THEN 1
    ELSE 0
  END) * 100.0 / COUNT(*), 2) AS negative_percentage
FROM ecommerce
GROUP BY brand
</pre>

#### Task 10 Retrieve a count of products for each primary category in the 'ecommerce' table

<pre>
SELECT primaryCategories,
  COUNT(*)
FROM ecommerce
GROUP BY primaryCategories
</pre>

#### Task 11 Retrieve all records from the 'ecommerce' table where the product name contains the word 'Tablet' as a substring

<pre>
SELECT *
FROM ecommerce
WHERE name LIKE "%Tablet%"
</pre>

#### Task 12 Count the number of product reviews in the 'ecommerce' table where the text contains the word 'Alexa' as a substring.

<pre>
SELECT COUNT(*)
FROM ecommerce
WHERE reviews_text LIKE "%Alexa%"
</pre>

