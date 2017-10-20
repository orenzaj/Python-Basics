## Menu Items:
# 'n', 'new challenge'
# 's', 'new step'
# 'd', 'delete a challenge'
# 'e', 'edit a challenge'

#Now create an OrderedDict named menu that has the menu items exactly as listed in the comment. Both keys and values will be strings.

from collections import OrderedDict

menu = OrderedDict([
    ('n', 'new challenge'),
    ('s', 'new step'),
    ('d', 'delete a challenge'),
    ('e', 'edit a challenge'),
])
