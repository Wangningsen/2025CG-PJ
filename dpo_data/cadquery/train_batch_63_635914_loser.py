import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-49))
r=w0.workplane(offset=-35/2).moveTo(49.5,-34).box(101,46,35).union(w0.sketch().push([(-91,70)]).circle(9).circle(4,mode='s').finalize().extrude(-14)).union(w0.sketch().push([(14,-34)]).circle(45).circle(43,mode='s').finalize().extrude(133))