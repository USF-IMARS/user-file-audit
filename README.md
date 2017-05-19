Users can request auditing of file accesses recording using an audit rule and reported using a cronjob + ausearch.

example crontab entries:

```cron
MAILTO="imarsroot@marine.usf.edu"

# NOTE: the use of `| mail ...` below *should* be superflous, but right now MAILTO seems to be failing on seashell.
# m  h  dom mon dow   command
 20  1  *   *   1     nice -n 15 /root/user-filewatches/watchreport.sh mahmoudFileWatch | mail -s "mahmoudFileWatch" imarsroot@marine.usf.edu
```
