import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,5))
r=w0.workplane(offset=-36/2).moveTo(-48,-84).cylinder(36,16).union(w0.workplane(offset=26/2).moveTo(39,75).cylinder(26,25))