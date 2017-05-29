#!/bin/bash

# prints report since last report was taken by this script

KEY=$1

# read last time (LAST_REPORT) reported from file
REPORT_FILE=/var/user-filewatch/$KEY
. $REPORT_FILE

# === print report to user
echo "reporting watch events since $LAST_REPORT"

echo "\n================================================\n"
echo "raw logfiles: `ls -l -h /var/log/audit/`"
echo "\n================================================\n"

echo "\t ausearch filewatch summary:"
echo "\t\t accessing users:"
echo `ausearch -i -k $KEY -ts $LAST_REPORT | /root/user-filewatches/auditparser/filewatch_summary.py`

echo "\t ausearch log results:"
echo `ausearch -i -k $KEY -ts $LAST_REPORT`  # TODO: don't do this twice.

# === save last report date
echo "LAST_REPORT=\""`date +"%m/%d/%Y %H:%M:%S"`\" > $REPORT_FILE
