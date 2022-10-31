import maya.cmds as cmds

sel = cmds.ls(sl=True)[0]

pos = cmds.xform(sel, q=True, ws=True, rotatePivot=True)

loc = cmds.spaceLocator(p=(0, 0, 0))[0]

cmds.xform(loc, ws=True, translation=pos)