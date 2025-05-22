import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,15))
w1=cq.Workplane('XY',origin=(0,0,16))
r=w0.sketch().arc((-57,-100),(-43,-68),(-6,-55)).arc((-84,-21),(-57,-100)).assemble().finalize().extrude(-31).union(w1.sketch().push([(64,66)]).circle(34).circle(9,mode='s').finalize().extrude(-31))