from .expr import *
from .mutation import *
from .relation import *

from typing import Union
wngStatement = Union[wngComplexExpr, wngAssignment, wngMutation]