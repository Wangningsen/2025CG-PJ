import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-48))
w1=cq.Workplane('XY',origin=(0,0,-84))
r=w0.workplane(offset=-16/2).moveTo(-91,70).cylinder(16,9).union(w0.sketch().push([(14,-34)]).circle(45).circle(43,mode='s').finalize().extrude(132)).union(w1.workplane(offset=35/2).moveTo(49.5,-34).box(101,46,35))