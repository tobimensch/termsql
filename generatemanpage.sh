#/bin/sh
export MORE_HELP=True
help2man -N ./termsql | gzip > termsql.1.gz
man2html ./termsql.1.gz > termsql_manpage.html
