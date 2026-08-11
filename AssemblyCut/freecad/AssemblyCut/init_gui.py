# -*- coding: utf-8 -*-
import os

import FreeCADGui as Gui

from . import Commands
from . import Manipulator

_ADDON_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_ICON = os.path.join(_ADDON_ROOT, "Resources", "Icons", "AssemblyCut.svg")


class AssemblyCutWorkbench(Gui.Workbench):
    MenuText = "Assembly Cut"
    ToolTip = "Cut multiple bodies with a single sketch"
    Icon = _ICON

    def Initialize(self):
        cmds = ["AssemblyCut_Cut"]
        self.appendToolbar("Assembly Cut", cmds)
        self.appendMenu("Assembly Cut", cmds)

    def GetClassName(self):
        return "Gui::PythonWorkbench"


Gui.addWorkbench(AssemblyCutWorkbench())
Gui.addWorkbenchManipulator(Manipulator.AssemblyCutManipulator())
