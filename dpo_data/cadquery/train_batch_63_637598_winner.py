import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-15))
w1=cq.Workplane('XY',origin=(0,0,-16))
r=w0.workplane(offset=16/2).moveTo(-52,-46).cylinder(16,18).union(w1.sketch().arc((-57,-100),(-42,-67),(-6,-55)).arc((-81,-18),(-57,-100)).assemble().push([(64,66)]).circle(34).circle(9,mode='s').finalize().extrude(31))