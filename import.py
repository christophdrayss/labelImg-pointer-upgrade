#
# exports a specific folder in the import directory to the google cloud
#
# Syntax:
# python3 import.py <GS URI> 
#  
# Example: 
# python3 import.py gs://bini-products-bucket/training-sets-2/intrusion/poc1_v1.2.0/frames
# 
#

import os
import sys

# uri
cloud_uri = sys.argv[1]

os.system('mkdir -p import')
os.system('gsutil -m cp -c -r '+cloud_uri+' ./import/')
