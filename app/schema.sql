-- users table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- previous submissions table
CREATE TABLE IF NOT EXISTS previous_submissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    submission TEXT NOT NULL,
    vulns TEXT, -- stores the logged vulnerabilities in JSON format
);
-- example structure of json data for the vulns column.
--{
--  "file_name": "example_code.py",
--  "vulnerabilities": [
--    {
--      "vulnerability": "SQL Injection",
--      "description": "User input is directly concatenated into the SQL query, making the code vulnerable to SQL Injection.",
--      "line_number": 42
--    },
--    {
--      "vulnerability": "Cross-Site Scripting (XSS)",
--      "description": "Unescaped user input is rendered into the HTML, leading to potential XSS attacks.",
--      "line_number": 78
--    },
--    {
--      "vulnerability": "Insecure Deserialization",
--      "description": "The code is deserializing untrusted data, which can lead to remote code execution.",
--      "line_number": 112
--    }
--  ]
--}
