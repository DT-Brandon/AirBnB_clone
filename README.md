# AirBnB clone project

## Usage:

In interactive mode
```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF   all   count   create   destroy   help   quit   show

(hbnb)
(hbnb)
(hbnb) quit
$
```
In non-interactive mode
```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF   all   count   create   destroy   help   quit   show

(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF   all   count   create   destroy   help   quit   show

(hbnb)
$
```
Classes defined
---------------
- BaseModel
- User
- Place
- State
- City
- Amenity
- Review

```bash
$ create <class>
$ all [<class>]
$ show <class> <id>
$ destroy <class> <id>
```
