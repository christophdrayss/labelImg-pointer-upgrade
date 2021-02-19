#
# exports a specific folder in the import directory to the google cloud
#
#

import os
import sys

def import_oci():
    if len(sys.argv) == 1:
        print("usage: import_oci [bucket] [storage prefix]")
        print("storage prefix is the path to the ressouce, e.g. 'labelling/poc1/'")
        print("you must have Oracle CLI installed: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm#Quickstart")
        return 

    bucket_name = sys.argv[1]
    cloud_prefix = sys.argv[2]

    print("bucket_name="+bucket_name)
    print("cloud_prefix="+cloud_prefix)

    os.system('mkdir -p import')
    os.system('oci os object bulk-download -bn '+bucket_name+' --prefix '+cloud_prefix+' --download-dir ./import/')

if __name__ == "__main__":
    import_oci()
