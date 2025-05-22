import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,59))
r=w0.sketch().arc((-96,-29),(-88,-33),(-92,-40)).arc((89,45),(-96,-29)).assemble().push([(-3,4)]).circle(48,mode='s').finalize().extrude(-118)