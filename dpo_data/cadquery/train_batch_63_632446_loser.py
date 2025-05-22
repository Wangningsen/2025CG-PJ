import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-46))
r=w0.sketch().arc((-9,-16),(-59,-79),(21,-58)).arc((59,-1),(-9,-16)).assemble().push([(28,-24)]).circle(2,mode='s').finalize().extrude(61).union(w0.workplane(offset=92/2).moveTo(-6,77).cylinder(92,23))