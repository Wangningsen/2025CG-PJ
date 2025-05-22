import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,16))
r=w0.workplane(offset=-116/2).moveTo(-40,-25).cylinder(116,52).union(w0.workplane(offset=84/2).moveTo(60,45).cylinder(84,32))