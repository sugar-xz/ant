from TestUnit.website.interface.user import User
from TestUnit.website.interface.org import Org
from TestUnit.website.interface.box import Box
from TestUnit.website.interface.ccs import Ccs
from TestUnit.website.interface.face import Face
from TestUnit.website.interface.guard import Guard
from TestUnit.website.interface.iot import Iot
from TestUnit.website.interface.map import Map
from TestUnit.website.interface.perm import Perm
from TestUnit.website.interface.public import Public
from TestUnit.website.interface.robot import Robot


class Common(User, Org, Box, Robot, Ccs, Face, Guard, Iot, Map, Perm, Public):
    pass
