import re


def increment_string(strng):
    last_num_regex = re.compile('[0-9]*$')
    last_num = last_num_regex.search(strng)
    suffix = '1'

    if len(last_num.group(0)) != 0:
        suffix = format(int(last_num.group(0)) + 1, '0' +
                        str(len(last_num.group(0))) + 'd')

    return strng[0:len(strng) - len(last_num.group(0))] + suffix


print(increment_string('abc12'))
print(increment_string('abc'))
print(increment_string('abc00'))
print(increment_string('abc099'))
