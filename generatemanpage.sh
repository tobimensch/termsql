#/bin/sh
MORE_HELP=True
help2man -N ./termsql | gzip > termsql.1.gz
