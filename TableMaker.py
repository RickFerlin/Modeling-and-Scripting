import maya.cmds as cmds

legHeight = 6
tableTopD = 13

cmds.polyCube(w=(legHeight/5), h=legHeight, d=(legHeight/5), sx=1, sy=1, sz=1, ax=(0, 1, 0), cuv=4, ch=1)
cmds.move((tableTopD - (legHeight/2)), (legHeight/2), ((tableTopD/2) - (legHeight/5)), r=1, os=1, wd=1)

cmds.polyCube(w=(legHeight/5), h=legHeight, d=(legHeight/5), sx=1, sy=1, sz=1, ax=(0, 1, 0), cuv=4, ch=1)
cmds.move((-1*(tableTopD - (legHeight/2))), (legHeight/2), ((tableTopD/2) - (legHeight/5)), r=1, os=1, wd=1)

cmds.polyCube(w=(legHeight/5), h=legHeight, d=(legHeight/5), sx=1, sy=1, sz=1, ax=(0, 1, 0), cuv=4, ch=1)
cmds.move((tableTopD - (legHeight/2)), (legHeight/2), (-1*((tableTopD/2) - (legHeight/5))), r=1, os=1, wd=1)

cmds.polyCube(w=(legHeight/5), h=legHeight, d=(legHeight/5), sx=1, sy=1, sz=1, ax=(0, 1, 0), cuv=4, ch=1)
cmds.move((-1*(tableTopD - (legHeight/2))), (legHeight/2), (-1*((tableTopD/2) - (legHeight/5))), r=1, os=1, wd=1)

cmds.polyCube(w=(tableTopD*2), h=(tableTopD/10), d=tableTopD, sx=1, sy=1, sz=1, ax=(0, 1, 0), cuv=4, ch=1)
cmds.move((0, (legHeight + ((tableTopD/10)/2)), 0), r=1, os=1, wd=1)
