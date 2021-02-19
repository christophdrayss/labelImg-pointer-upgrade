#
# exports a specific folder in the import directory to the Oracle cloud
#
#

import os
import sys

def export_oci():
    if len(sys.argv) == 1:
        print("usage: export_oci [local_folder] [bucket] [storage prefix]")
        print("storage prefix is the path to the ressouce, e.g. 'labelling/poc1/'")
        print("you must have Oracle CLI installed: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm#Quickstart")
        return

    local_folder = sys.argv[1]
    bucket_name = sys.argv[2]
    cloud_prefix = sys.argv[3]

    print("local_folder="+local_folder)
    print("bucket_name="+bucket_name)
    print("cloud_prefix="+cloud_prefix)

    os.system('mkdir -p import')
    os.system('oci os object bulk-upload -bn '+bucket_name+' --object-prefix '+cloud_prefix+' --src-dir ./import/'+local_folder)

if __name__ == "__main__":
    export_oci()
