import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,96))
r=w0.sketch().arc((-96,-40),(93,-24),(-35,95)).segment((-38,95)).segment((-38,94)).arc((-57,85),(-77,68)).arc((-9,3),(-96,-40)).assemble().push([(18.5,-75.5)]).rect(11,7,mode='s').finalize().extrude(-192)