--Create Table
CREATE TABLE tableName (
    id INT PRIMARY KEY,
    date DATE,
    company NVARCHAR(255),
    open FLOAT,
    close FLOAT,
    high FLOAT,
    low FLOAT,
    volume BIGINT
);

--Create index for better reads
CREATE INDEX idx_date_company ON tableName (date, company);

--Daily Price Variation
SELECT company, date, (close - open) AS price_variation
FROM tableName
WHERE date = '2024-07-01'

--Volume Change
SELECT company, date, volume
FROM tableName
WHERE date = '2024-07-01'
ORDER BY company, date;

-- Median Variation
SELECT date, PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY (close - open)) AS median_variation
FROM tableName
GROUP BY date;