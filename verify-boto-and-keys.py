
#some code goes here
import boto
import urllib2

response = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')

html=response.read()

result = html.split(':')

for line in result:
	print line

print(boto.Version)

