# This script created a queue
#
# Author - Raminta Zelvyte  Nov 2015
#
#
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2

# Get the keys from a specific url and then use them to connect to AWS Service

response = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')

html=response.read()

result = html.split(':')

#print (result[0])
#print (result[1])

access_key_id = result[0]
secret_access_key = result[1]

#print (access_key_id,secret_access_key)
# Set up a connection to the AWS service.
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

#student_number = 'C13526123'
#conn.delete_queue(sys.argv[1])

# Get a list of the queues that exists and then print the list out
rs = conn.get_all_queues()

#python consume.py <id>
#python consume.py read <id>
#python consume.py consume <id>

if(sys.argv[1]=="read"):
	for q in rs:
        	if (q.id==sys.argv[2]):
                	print "reading messages..."
                	rs = q.get_messages()
                	m = rs[0]
               	 	print ('My message is:' + m.get_body())


if(sys.argv[1]=="consume"):
	for q in rs:
		if (q.id==sys.argv[2]):
			print "Consuming message..."
			rs = q.get_messages()
			m = rs[0]
			q.delete_message(m)
			print ('Message  deleted  from  the  queue')
