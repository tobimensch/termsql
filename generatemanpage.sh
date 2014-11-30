#/bin/sh
export MORE_HELP=True
cli2man ./termsql -o auto --gzip --info-section examples -I manpage_additional_info
cat termsql.1.gz | gunzip | mandoc -Thtml > termsql_manpage.html
