import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,15))
r=w0.sketch().arc((-57,-100),(-41,-66),(-6,-55)).arc((-82,-19),(-57,-100)).assemble().push([(64,66)]).circle(34).circle(9,mode='s').finalize().extrude(-31)