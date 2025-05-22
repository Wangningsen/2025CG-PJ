import cadquery as cq
w0=cq.Workplane('YZ',origin=(-24,0,0))
w1=cq.Workplane('YZ',origin=(-18,0,0))
r=w0.sketch().segment((-25,-39),(15,-61)).segment((19,-53)).arc((10,-4),(55,25)).segment((69,39)).segment((30,61)).close().assemble().finalize().extrude(-76).union(w0.workplane(offset=-9/2).moveTo(-66,-52).cylinder(9,3)).union(w1.sketch().push([(22,0)]).rect(28,22).push([(33,-1)]).rect(4,2,mode='s').finalize().extrude(118))