import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,65))
r=w0.workplane(offset=-130/2).moveTo(37,78).cylinder(130,22).union(w0.workplane(offset=-114/2).moveTo(0,-12).cylinder(114,88))