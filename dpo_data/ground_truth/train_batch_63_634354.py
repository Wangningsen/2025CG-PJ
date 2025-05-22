import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,12))
r=w0.workplane(offset=-50/2).moveTo(35,-64).cylinder(50,36).union(w0.sketch().segment((-71,-65),(28,-65)).segment((7,-50)).segment((25,-22)).segment((48,-37)).segment((48,100)).segment((-71,100)).close().assemble().push([(-4,61)]).rect(42,12,mode='s').finalize().extrude(25))