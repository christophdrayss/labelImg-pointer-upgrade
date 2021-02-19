#
# exports a specific folder in the import directory to the google cloud
#
# Syntax:
# python3 export.py <FOLDER NAME IN IMPORT FOLDER> <GS URI> 
#  
# Example: 
# python3 export.py 2021-02-frames_301 gs://bini-products-bucket/training-sets-2/intrusion/poc1_v1.2.0/frames
#
#

import os
import sys

# folder name
dir_name = sys.argv[1]

# uri
cloud_uri = sys.argv[2]

os.system('gsutil -m cp -c -r ./import/'+dir_name+' '+cloud_uri)
