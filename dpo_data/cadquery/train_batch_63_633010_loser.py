import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,14))
w1=cq.Workplane('XY',origin=(0,0,36))
r=w0.workplane(offset=-83/2).moveTo(32,-54).cylinder(83,35).union(w0.sketch().segment((9,-100),(55,-100)).segment((55,-12)).arc((31,-29),(9,-7)).close().assemble().push([(26,-93)]).circle(11,mode='s').finalize().extrude(55)).union(w1.workplane(offset=-82/2).moveTo(-10,43).cylinder(82,57))