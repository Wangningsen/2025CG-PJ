import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,45))
r=w0.workplane(offset=-91/2).moveTo(-53.5,-90.5).box(45,19,91).union(w0.workplane(offset=-59/2).moveTo(14,38).cylinder(59,62))