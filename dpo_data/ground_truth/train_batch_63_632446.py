import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-46))
r=w0.sketch().arc((-8,-16),(-57,-82),(21,-58)).arc((58,0),(-8,-16)).assemble().push([(28,-22)]).circle(2,mode='s').finalize().extrude(61).union(w0.workplane(offset=92/2).moveTo(-6,77).cylinder(92,23))