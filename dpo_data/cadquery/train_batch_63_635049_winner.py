import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-20,0))
r=w0.workplane(offset=-19/2).moveTo(-41,-80).cylinder(19,20).union(w0.workplane(offset=58/2).moveTo(20,54).cylinder(58,46)).union(w0.workplane(offset=59/2).moveTo(-15,-7).cylinder(59,51))