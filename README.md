# Description

Differential analysis of sqlite files based on primary key (rowid)

Detects changes between versions of sqlite files:

- **Database Table**
  - Table created
  - Table deleted
- **Table Row**
  - Row created
  - Row modified
  - Row deleted

# Installation

`pip install sqlitediff`

# Usage

**From command line:**

`python -m sqlitediff --pathBefore PATHBEFORE --pathAfter PATHAFTER [--primaryKey PRIMARYKEY]`

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--pathBefore | -b | String | - | Path to sqlite file before action |
|--pathAfter | -a | String | - | Path to sqlite file after action |
|--primaryKey | -p | String | rowid | Name of the primary key column |
|--printSnapshot | -s | String | - | before = Prints the before snapshot <br> after = Prints the after snapshot |


# Example

`python -m sqlitediff -b path/to/before.db -a path/to/after.db`

```
################################################################################

sqlitediff by 5f0
Differential analysis of sqlite files

Current working directory: path/to/sqlitediff

Sqlite file before action:
-->    Path: path/to/before.db
-->     MD5: d7e88c55c4ec6ed7cd7fa6c6cb8b0b45
-->  SHA256: 19722a52443837b2cc7ac77fa806da6f2e1f307707ac8a2fdfe6a5c097758faf

Sqlite file after action:
-->    Path: path/to/after.sqlite
-->     MD5: 305d12c0b2b49b149a508d9d4cb7d573
-->  SHA256: 3073be75fb6b0ace2ffc94332c2c77e1fe12c6f618c840c122112a61ee63585a

Datetime: 01/01/1970 11:12:13

################################################################################

Table Analysis
---

--> Tables before: 
         --- 
         List: ['dog', 'fish']
         --- 
         Name: dog
         Rows: 2
         --- 
         Name: fish
         Rows: 4
         --- 

--> Tables after: 
         --- 
         List: ['fish', 'snowman']
         --- 
         Name: fish
         Rows: 5
         --- 
         Name: snowman
         Rows: 1
         --- 

--> Deleted Tables: 
         --> ['dog']

--> Created Tables: 
         --> ['snowman']


Row Analysis
---

--> snowman
    ---
    Colums:
    ---
     --> ['id', 'name', 'species', 'fridge']
    ---
    Created: [1]
    ---
     --> (1, 'olaf', 'snow', 1)
    ---

--> dog
    ---
    Colums:
    ---
     --> ['id', 'name', 'species', 'garden']
    ---
    Deleted: [1, 2]
    ---
     --> (1, 'Bill', 'shepard', 1)
     --> (2, 'Tom', 'little', 7)
    ---

--> fish
    ---
    Colums:
    ---
     --> ['id', 'name', 'species', 'tank']
    ---
    Created: {5, 6}
    ---
     --> (5, 'Leo', 'whale', 3)
     --> (6, 'Ole', 'delfin', 4)
    ---
   Updated: [2, 4]
    ---
     --> (2, 'Jamie', 'cuttlefish', 7)
     --> (2, 'Jamie', 'cuttlefish', 77)
    ---
     --> (4, 'Mark', 'bigfish', 9)
     --> (4, 'Mark', 'bigfish', 99)
    ---
    Deleted: {1}
    ---
     --> (1, 'Sammy', 'shark', 1)
    ---

################################################################################

Execution Time: 0.010948 sec

```

`python -m sqlitediff -b path/to/before.db -a path/to/after.db -s before`

```
################################################################################

sqlitediff by 5f0
Differential analysis of sqlite files

Current working directory: path/to/sqlitediff

Sqlite file before action:
-->    Path: path/to/before.db
-->     MD5: d7e88c55c4ec6ed7cd7fa6c6cb8b0b45
-->  SHA256: 19722a52443837b2cc7ac77fa806da6f2e1f307707ac8a2fdfe6a5c097758faf

Sqlite file after action:
-->    Path: path/to/after.sqlite
-->     MD5: 305d12c0b2b49b149a508d9d4cb7d573
-->  SHA256: 3073be75fb6b0ace2ffc94332c2c77e1fe12c6f618c840c122112a61ee63585a

Datetime: 01/01/1970 11:12:13

################################################################################

Snapshot Name: before
---
   Table Name: fish
         Rows: 4
      Columns: ['id', 'name', 'species', 'tank']
   Row Values: 
          --- 
           --> (1, 'Sammy', 'shark', 1)
           --> (2, 'Jamie', 'cuttlefish', 7)
           --> (3, 'Carl', 'goldfish', 8)
           --> (4, 'Mark', 'bigfish', 9)
          --- 
---
   Table Name: dog
         Rows: 2
      Columns: ['id', 'name', 'species', 'garden']
   Row Values: 
          --- 
           --> (1, 'Bill', 'shepard', 1)
           --> (2, 'Tom', 'little', 7)
          --- 
---

################################################################################

Execution Time: 0.010948 sec


```


# License

MIT