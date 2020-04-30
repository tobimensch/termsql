TERMSQL
=======

Convert text from a file or from stdin into SQL table and query it instantly. Uses sqlite as backend.
The idea is to make SQL into a tool on the command line or in scripts.

Install
=======

Requirements:
 - python
 - sqlite3
 - sqlparse module 0.1.15 and up from https://github.com/andialbrecht/sqlparse (optional)

To install termsql open a terminal and run:

    sudo python setup.py install

Termsql now supports shorter and more convenient sql statements given the sqlparse module from https://pypi.python.org/pypi/sqlparse/ version 0.1.15 or higher is installed.

    termsql "select col0,col1 from tbl"
    #is equal to:
    termsql select col0,col1
    
    termsql -m line -1 "select USER,COUNT(*) from tbl group by USER"
    #is equal to:
    termsql -m line -1 "select USER,COUNT(*) group by USER"

Therefore installing the sqlparse module (which is tiny anyway) from https://pypi.python.org/pypi/sqlparse/ or
https://github.com/andialbrecht/sqlparse is highly recommended. At least if you want to save yourself some typing.

Learn more
==========

always helpful is:

    termsql --help
  
and also:

    man termsql
  
Online manual:

  http://tobimensch.github.io/termsql

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

Examples
========

    export LC_ALL=en_US; top -b | head | termsql -1 -H 6 "select [PID],[USER],[COMMAND],[%CPU] from tbl where [%CPU]>=25"

> termsql doesn't recognize numbers like "25,3" as numbers, but as strings. export LC_ALL=en_US ensures that top outputs numbers that are easy for termsql/sqlite to digest (ie. "25.3"). -H 6 makes termsql disregard the first 6 lines. We select only the processes with more than 25% cpu usage and output their PID,USER,COMMAND and %CPU.

    export DISPLAY=$(ps aux | termsql "select COL11 from tbl where COL10 like '%Xorg.bin%' limit 1")

> set DISPLAY environment variable to what display X is running on right now, assuming that the X binary is called "Xorg.bin")

    ls -lha /usr/bin/* | termsql -w -r 8 "select * from tbl order by COL8 desc"

> -r 8 merges the filenames into the 8th column. Then "order by COL8 desc" sorts them in reverse order. Due to -w the output looks nice on the command line

    ps aux | termsql -m line -1 "select USER,COUNT(*) from tbl group by USER"

> counts the total number of processes that each user has running. -1 gets the column names from the first line, therefore we can use USER instead of COL0 in the SQL statement. "group by USER" groups the rows of with identical USER together and for that reason COUNT(*) returns the total number of rows (in this case processes) for each USER. -m line beautifies the output.

    termsql -ei .config/Bitcoin/Bitcoin-Qt.conf -c key,value -d = -p = -x "update tbl set value='true' where key='fMinimizeToTray'"

> Demonstrates how you can use termsql to edit simple config files with key/value pairs. -i loads the config file as input and -e makes sure this same file is written to instead of stdout. Simply speaking: enabling edit mode. -d = sets the delimiter for splitting the input to = and -p = sets the separator for the output to = again, so that the output format matches the input format. -x appends a ";select * from tbl" to the user defined query, so that we get everything back that we put in. The user query is an SQL update statement which sets the value part of the key value pair to true, where the key is fMinimizeToTray. -c key,value allows us to use these convenient names instead of COL0 (key) and COL1 (value). Note that this approach may not always be perfect, for example in .config/Bitcoin/Bitcoin-Qt.conf there's a section line "[General]" which gets changed to "[General]=" after termsql is done with editing. Which may or may not be a problem depending on the program that uses the config file. It could easily be fixed with a tool like sed though.

For detailed information about options and more examples see the [Manual](http://tobimensch.github.io/termsql)

Vs awk
======

- awk can't create permanent sqlite databases
- sqlite is efficient, fast and mature (not saying that awk isn't)
- many people have worked with SQL before that aren't experts on awk
- SQL tends to look very descriptive, which should make it easy to maintain code and fix bugs
- termsql is designed from the start to be as intuitive as possible,
  awk doesn't really strike the author of termsql as intuitive (that's a personal opinion and
  not a fact).
- termsql can output to CSV,HTML,insert,SQL dump,tcl,text,line,SQlite database

Contribute
==========

You like termsql and want to help in some way? Then why don't you tell others about it and show them how
they can use it. Post your termsql usecases and ideas on twitter, facebook, google+, your-favorite-social-media,
your blog or website. Making termsql more popular is a great contribution.

Another possible way to contribute is to help with improvement or translation of the documentation.

It would also be great, if people create packages for their own distribution or file bugreports
for their distribution, so that termsql will be available in their favorite (Linux-)distribution.

Of course contributing code/patches is also welcome, look at the roadmap below or at the issues tracker on github
for ideas on what to do or come up with your own ideas. Forking termsql is a great way to start as well.

Want to contribute by reporting a problem/bug? Feel free to use [the issue tracker](https://github.com/tobimensch/termsql/issues).

Roadmap
=======

- ~~it's not documented in the man page yet~~, but termsql supports shorter SQL statements,
  where "from tbl" and other repetitive text isn't required anymore.
  - "select col0,col1 where col1='foo'" => "select col0,col1 from tbl where col1='foo'"
    - this particular feature is now commited and working given that you have sqlparse module version 0.1.15 and up
  - "set foo='X' where bar='Y'" => "update tbl set foo='X' where bar='Y'" 
    - DONE
  - "where col4 like '%sometext%' => "select * from tbl where col4 like '%sometext%'"
    - DONE
  - Saving users some typing.
  - Making commands more concise.
- type SQL commands without quotes
  - termsql -i input.txt select col3
    - DONE
  - quotes around the whole statement will continue to be recommended because you'll have to escape special charactes in the shell like this:

    termsql -i input.txt select col3 from tbl where col0="\'test  spaces\'" \; select col 1 from tbl

- add more examples to manual
- support user scripts to preprocess column input
  - this would allow users to use tools like sed or anything they can think of to modify certain columns BEFORE they're inserted into the database

    termsql -i input.csv -d ':' --pp 3 my_script.sh "select * from tbl where col5>=100"
 
  - my_script.sh would receive the column data, the row number and the col number as input

- get input from users how to improve further / what features to adds
- prepare source/make packages for different distributions and OSs
  - help/contributions welcome!

<!--
- idea: support presets for certain well defined tasks
 - some presets could come with termsql, and the user could also define his own
 - example of possible presets **(NOTE: all of this is hypothetical mockup code)**:

``` shell
    #preset for editing a INI style config
    termsql -i config.txt --pre ini "set value='false' where key='getgoing'" 
    #preset for running a script on a certain column before it's inserted into the database
    termsql --pre mod_col 3 mycol_modding.sh "select col3 where table
    #print list of all presets
    termsql --print-presets

```
-->

