from itertools import product
from textwrap import shorten
from unicodedata import name
from models import User, Product, ProductTag, Tag, db, Transaction


def create_users_and_products():
    piet = User.create(
        name='piet',
        address='zeestraat 5, ossdorp')
    babs = User.create(
        name='babs',
        address='strandweg 2, boulevard')
    mike = User.create(
        name='mike',
        address='straatweg 14, strand')
    nova = User.create(
        name='nova',
        address='duinweg 4, de duinen')
    kees = User.create(
        name='kees',
        address='kustweg 55, het strand')

    plank = Product.create(
        name='plank',
        price_per_item=25,
        quantity=10,
        description='plank voor in de golven',
        owner=mike
    )

    fin = Product.create(
        name='fin',
        price_per_item=10,
        quantity=7,
        description='een fin om in balans te blijven',
        owner=nova
    )

    horloge = Product.create(
        name='horloge',
        price_per_item=5,
        quantity=15,
        description='getijen en tijd ',
        owner=kees
    )

    oordop = Product.create(
        name='oordop',
        price_per_item=5,
        quantity=15,
        description='tegen water ',
        owner=kees
    )

    leash = Product.create(
        name='leash',
        price_per_item=10,
        quantity=15,
        description='lijn die vast zit aan je plank',
        owner=piet
    )

    finbox = Product.create(
        name='finbox',
        price_per_item=2.50,
        quantity=10,
        description='waar de fin in zit',
        owner=mike
    )

    wetsuit = Product.create(
        name='wetsuit',
        price_per_item=11.95,
        quantity=4,
        description='pak om langer mee in het water te liggen',
        owner=babs
    )

    schoenen = Product.create(
        name='schoenen',
        price_per_item=7.50,
        quantity=10,
        description='warme voeten',
        owner=babs
    )

    short = Product.create(
        name='short',
        price_per_item=35,
        quantity=6,
        description='korte broek',
        owner=kees
    )

    wax = Product.create(
        name='wax',
        price_per_item=40,
        quantity=4,
        description='betere grip voor op je plank',
        owner=kees
    )

    waxcrabber = Product.create(
        name='waxcrabber',
        price_per_item=40,
        quantity=4,
        description='haaltb de wax van je plank',
        owner=kees
    )
    surfbag = Product.create(
        name='surfbag',
        price_per_item=50,
        quantity=2,
        description='beschreming van je plank tijdens vervoer',
        owner=piet
    )

    surfzak = Product.create(
        name='surfzak',
        price_per_item=50,
        quantity=2,
        description='om je natte wetsuit in te stoppen',
        owner=piet
    )

    surfaccessoires = Tag.create(name='surfaccessoires')
    surfbeschreming = Tag.create(name='surfbeschreming')
    plankbenodigdheden = Tag.create(name='plankbenodigdheden')
    wetsuitbenodigdheden = Tag.create(name='wetsuitbenodigdheden')
    kleding = Tag.create(name='kleding')

    ProductTag.create(product=oordop, tag=surfaccessoires)
    ProductTag.create(product=waxcrabber, tag=surfaccessoires)
    ProductTag.create(product=wax, tag=surfaccessoires)
    ProductTag.create(product=horloge, tag=surfaccessoires)
    ProductTag.create(product=surfzak, tag=surfbeschreming)
    ProductTag.create(product=surfbag, tag=surfbeschreming)
    ProductTag.create(product=surfbag, tag=surfbag)
    ProductTag.create(product=fin, tag=plankbenodigdheden)
    ProductTag.create(product=plank, tag=plankbenodigdheden)
    ProductTag.create(product=leash, tag=plankbenodigdheden)
    ProductTag.create(product=finbox, tag=plankbenodigdheden)
    ProductTag.create(product=wetsuit, tag=wetsuitbenodigdheden)
    ProductTag.create(product=schoenen, tag=wetsuitbenodigdheden)
    ProductTag.create(product=short, tag=kleding)


db.create_tables([User, Product, Tag, ProductTag, Transaction])

create_users_and_products()
