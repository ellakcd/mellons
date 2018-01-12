############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, name, is_bestseller=False 
                 ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    musk_melon = MelonType('musk', 1998, 'green', True, 'Muskmelon', True)
    musk_melon.add_pairing('mint')
    all_melon_types.append(musk_melon)

    casaba = MelonType('cas', 2003, 'orange', False, 'Casaba')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green', False, 'Crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    watermellon = MelonType('yw', 2013, 'yellow', False, 'Watermellon', True)
    watermellon.add_pairing('ice cream')
    all_melon_types.append(watermellon)



    # Fill in the rest

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print '{name} pairs with'.format(name=melon.name)
        for good_pair in melon.pairings:
            print '- {good_pair}'.format(good_pair=good_pair)
        print '\n'

    # Fill in the rest

melon_types = make_melon_types()
print_pairing_info(melon_types)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_lookup = {}
    for melon in melon_types:
        melon_lookup[melon.code] = melon # __repr__ to prettify the value

    return melon_lookup
    # Fill in the rest

melon_types = make_melon_type_lookup(melon_types)
############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, variety, shape_rate, color_rate, field, harvester):
        self.variety = variety
        self.shape_rate = shape_rate
        self.color_rate = color_rate
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        if self.field != 3 and self.shape_rate > 5 and self.color_rate > 5:
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    melon_objects = []

    melon1 = Melon(melon_types['yw'], 8, 7, 2, 'Sheila')
    melon_objects.append(melon1)

    melon2 = Melon(melon_types['yw'], 3, 4, 2, 'Sheila')
    melon_objects.append(melon2)

    melon3 = Melon(melon_types['yw'], 9, 8, 3, 'Sheila')
    melon_objects.append(melon3)

    melon4 = Melon(melon_types['cas'], 10, 6, 35, 'Sheila')
    melon_objects.append(melon4)

    melon5 = Melon(melon_types['cren'], 8, 9, 35, 'Michael')
    melon_objects.append(melon5)

    melon6 = Melon(melon_types['cren'], 8, 2, 35, 'Michael')
    melon_objects.append(melon6)

    melon7 = Melon(melon_types['cren'], 2, 3, 4, 'Michael')
    melon_objects.append(melon7)

    melon8 = Melon(melon_types['musk'], 6, 7, 4, 'Michael')
    melon_objects.append(melon8)

    melon9 = Melon(melon_types['yw'], 7, 10, 3, 'Sheila')
    melon_objects.append(melon9)

    return melon_objects

harvest_melons = make_melons(melon_types)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
    for melon in melons:
        print 'Melon: {name}'.format(name=melon.variety.name)
        print 'Harvested by {harvester} in Field {field}'.format(harvester=melon.harvester, field=melon.field)
        if melon.is_sellable():
            print 'Sellable!'
        else:
            print 'Danger! Do not sell!'

get_sellability_report(harvest_melons)


def add_melons_from_text(filepath):

    document = open(filepath)
    melon_objects = []

    for line in document:

        line.rstrip()
        words = line.split()
        shape = words[1]
        color = words[3]
        variety = words[5]
        harvester = words[8]
        field = words[-1]

        melon_objects.append(Melon(melon_types[variety], shape, color, field, harvester))

    return melon_objects


print add_melons_from_text("harvest_log.txt")