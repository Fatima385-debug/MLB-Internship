Project Overview
A simple student record management system built with core Python, using an in-memory list of dictionaries as the data store. No file storage is used 

Core Features
-Add Student
-View All Students
-Search Student (by Name or Roll Number)
-Update Student Information
-Delete Student

Bonus Features Implemented
-Input Validation (non-empty names, positive numeric roll no./age, duplicate roll number check)
-Menu-Driven Interface (loops until user chooses Exit)
-Search by Roll Number (dedicated option in the search menu)
-Display Total Number of Students

What I Learned Today
-How to model real-world records using a list of dictionaries, where each dictionary represents one student and the list represents the whole table of students.
-How to write reusable validation functions instead of repeating validation logic in every menu option.
-How to structure a menu-driven CLI application using a while True loop combined with if/elif branching, and how to cleanly exit the loop.
-How to safely remove an item from a list of dictionaries without breaking iteration, and why using list.remove() on the matched dictionary object is simpler than filtering by index.


Challenges Faced & Solutions Implemented
-Users could enter blank names or non-numeric ages/roll numbers, crashing the program. Wrote dedicated validation helper functions that loop until valid input is given. 
-Needed to prevent two students from sharing the same roll number. Added a roll_number_exists() check before inserting a new student in add_student(). 
-Updating a record required letting the user skip fields they don't want to change. Used empty-input checks if new_value: so pressing enter keeps the existing value instead of overwriting it. 
Deleting the wrong student by mistake. Added a confirmation prompt before actually removing the record. 

