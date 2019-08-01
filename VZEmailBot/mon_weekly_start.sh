#!/usr/bin/env bash

for host in vci-core-task{1..3}.sfdc.wavemarket.com; do echo $host; ssh -q $host "date; grep 'Starting com.wavemarket.finder.common.task.CNIWeeklyEmailSummaryTask' /opt/wm/log/finder-verizon-core.log"; done > mon_weekly_start.txt
cat mon_weekly_start.txt
