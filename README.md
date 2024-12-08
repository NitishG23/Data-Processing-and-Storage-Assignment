# Data-Processing-and-Storage-Assignment

This repository provides an in-memory key-value database that supports basic transactions. Below are instructions to run the code. 

## Prerequisites

**Python 3**:  
  Make sure you have Python 3 installed. To check, run:
  ```
  python3 --version
  ```

## Setup:
Download or clone the Repository:
Make sure you have the file inmemory_db.py in a directory on your machine. If you are using Git:

```
git clone https://github.com/YourUsername/YourRepository.git
```

Or download the ZIP file from the repository and extract it

Navigate to the directory containing inmemory_db.py:
```
cd YourRepository
```

Start Python:
In your terminal run this:
```
python3
```

Import and initialize the database:
Inside the terminal (you will see the >>> prompt):
```
from inmemory_db import InMemoryDB
db = InMemoryDB()
```

## Example of Usage 
After putting the code above in the python file. In the same python file put:
```
print(db.get("A"))   # Expected output: None
db.begin_transaction()
db.put("A", 5)
print(db.get("A"))   # Expected output: None
db.commit()
print(db.get("A"))   # Expected output: 5
```

## Assignment Modifications
To improve this assignment to be an actual assignment, I would recommend putting more specific directions for each of the methods and also providing test cases for the student to run to ensure everything is working fine in their code. Adding onto that, it would be a good part 2 to the code-writing to also make the student write test cases for themselves and submit them as it would cover another important software engineering aspect. To expand the assignment, there could be additional functions such as delete(key) to allow removal of keys as that seems fairly significant. Lastly, since this is one of the only coding assignments in the class, there should be a heavy emphasis on writing proper documentation and commenting code. 



