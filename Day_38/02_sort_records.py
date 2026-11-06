#ORDER BY — Sort records
#Use ORDER BY to sort records.

# SELECT * FROM students
# ORDER BY marks ASC;



# LIMIT — Restrict results
# Use LIMIT to display a fixed number of records.

#SELECT * FROM students
#LIMIT 3;



# Aggregate functions

#SELECT COUNT(*) FROM students;

#SELECT AVG(marks) FROM students;

#SELECT MAX(marks) FROM students;

#SELECT MIN(marks) FROM students;

# SELECT SUM(marks) FROM students;




# GROUP BY — Group records

# SELECT course, COUNT(*)
# FROM students
# GROUP BY course;




# HAVING — Filter groups
# HAVING filters grouped results. It is commonly used with aggregate functions.

# SELECT course, AVG(marks)
# FROM students
# GROUP BY course
# HAVING AVG(marks) > 70;