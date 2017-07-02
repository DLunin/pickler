from .pickler import *

ip = get_ipython()
ip.register_magics(PicklerMagic)

