import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,40))
w1=cq.Workplane('XY',origin=(0,0,52))
r=w0.sketch().segment((24,33),(100,33)).segment((100,62)).segment((25,62)).arc((-50,49),(24,33)).assemble().push([(-11,48)]).circle(20,mode='s').finalize().extrude(-92).union(w1.workplane(offset=-9/2).moveTo(-75,-73.5).box(50,27,9))