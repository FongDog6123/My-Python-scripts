#!/usr/bin/env bash

for host in <specified host>; do echo $host; ssh -q $host "date; grep 'Starting <omitted>"; done > emailscript.txt
cat emailscript.txt
