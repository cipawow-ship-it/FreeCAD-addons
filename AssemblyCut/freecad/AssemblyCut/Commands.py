# -*- coding: utf-8 -*-
import os

import FreeCAD
import FreeCADGui as Gui

_ADDON_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_ICON = os.path.join(_ADDON_ROOT, "Resources", "Icons", "AssemblyCut.svg")


class AssemblyCutCommand:
    def GetResources(self):
        return {
            "MenuText": "Assembly Cut",
            "ToolTip": "Cut multiple bodies with a selected sketch",
            "Pixmap": _ICON,
        }

    def Activated(self):
        from .AssemblyCutCore import assembly_cut

        assembly_cut()

    def IsActive(self):
        try:
            doc = FreeCAD.ActiveDocument
            if doc is None:
                return False
            sel = Gui.Selection.getSelection()
            if not sel:
                return False
            return "Sketch" in sel[0].TypeId
        except Exception:
            return False


Gui.addCommand("AssemblyCut_Cut", AssemblyCutCommand())
