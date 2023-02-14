import json
import ast
import argparse

def getKey(obj):
    keys = list(obj)
    if len(keys) != 1:
        raise Exception('either multiple keys or empty dict found')
    else:
        return keys[0]


def getNestedValue(obj, key, isFound = False):
    # print(obj, key, isFound)
    if type(obj) is not dict and not isFound:
        print(type(obj), isFound)
        return None
    if (isFound or (key in obj.keys())) :
        if type(obj[key]) is dict:
            return getNestedValue(obj[key], getKey(obj[key]), True)
        else:
            # print(f'obj[getKey(obj)]: {obj[getKey(obj)]}')
            return obj[getKey(obj)]
    else:
        nestedKey = getKey(obj)
        return getNestedValue(obj[nestedKey], key, False)

if __name__ == '__main__':

    """Getting input from the user as an argument
    """
    parser = argparse.ArgumentParser(add_help=True, usage='%(prog)s [options]',
                                     description='Get meatadata of the Items')
    parser.add_argument('-ob', '--object', dest='object', default='{"a": {"b": {"c": "d"}}}', type=str,
                        help='Please enter the nested dictionary object (default: %(default)s)')
    parser.add_argument('-k', '--key', dest='key', default='c',
                        help='Please enter the key for the object (default: %(default)s)')
    args = parser.parse_args()

    json_obj = json.loads(args.object)
    print('obj type', type(json_obj))

    value = getNestedValue(json_obj, args.key)
    print(value)