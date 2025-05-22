import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-67))
r=w0.workplane(offset=45/2).moveTo(77,-23).box(46,136,45).union(w0.workplane(offset=134/2).moveTo(-34,25).cylinder(134,66))