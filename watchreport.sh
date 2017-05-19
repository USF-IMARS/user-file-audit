#!/bin/bash

# prints report since last report was taken by this script

KEY=$1

# read last time (LAST_REPORT) reported from file
REPORT_FILE=/var/user-filewatch/$KEY
. $REPORT_FILE

echo "reporting watch events since $LAST_REPORT"

echo "\n================================================\n"

echo "raw logfiles: `ls -l -h /var/log/audit/`"

echo "\n================================================\n"

echo `nice -n 15 ausearch -k $KEY -ts $LAST_REPORT`

echo "LAST_REPORT=\""`date +"%m/%d/%Y %H:%M:%S"`\" > $REPORT_FILE
