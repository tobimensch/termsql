termsql
=======

Convert text from a file or from stdin into SQL table and query it instantly. Uses sqlite as backend.
The idea is to make SQL into a tool on the command line or in scripts.

install
=======

run:
  sudo python setup.py install

learn more
==========

always helpful is:
  termsql --help
  
and also:
  man termsql

So what can it do?
==================

- convert text/CSV files into sqlite database/table
- work on stdin data on-the-fly
- it can be used as swiss army knife kind of tool for extracting information
  from other processes that send their information to termsql via a pipe
  on the command line or in scripts
- termsql can also pipe into another termsql of course
- you can quickly sort and extract data
- creates string/integer/float column types automatically
- gives you the syntax and power of SQL on the command line
