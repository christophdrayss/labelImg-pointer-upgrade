import os
import sys

import_uri = sys.argv[1]

os.system('gsutil cp -r '+import_uri+' ./import ')