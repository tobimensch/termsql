#/bin/sh
export MORE_HELP=True
help2man --include=manpage_additional_info --source=https://github.com/tobimensch/termsql -N ./termsql | gzip > termsql.1.gz
man2html -r ./termsql.1.gz > termsql_manpage.html
