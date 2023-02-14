import json
import os
import boto3
from dateutil.parser import parse
import datetime
import argparse
from botocore.exceptions import ClientError


def get_metadata(metadataItem):
    cmd = 'curl http://169.254.169.254/latest/meta-data/{name}'.format(name = metadataItem)
    system_output = os.system(cmd)
    json_output = json.dumps(system_output)
    print(json_output)

def main():
    """Getting input from the user as an argument
    """
    parser = argparse.ArgumentParser(add_help=True, usage='%(prog)s [options]',
                                     description='Get meatadata of the Items')
    parser.add_argument('-m', '--metadataItem', dest='metadataItem',
                        help='Please enter the metadata item name(default: %(default)s)')
    parser.add_argument('-i', '--itemNames', dest='itemNames', action='store_false',
                        help='It will print item names of metadata')
    args = parser.parse_args()

    if args.metadataItem:
       get_metadata(args.metadataItem)
    elif not args.itemNames:
       cmd = 'curl http://169.254.169.254/latest/meta-data'
       os.system(cmd)
    else:
        print('Invalid Input!')


if __name__ == '__main__':
    main()