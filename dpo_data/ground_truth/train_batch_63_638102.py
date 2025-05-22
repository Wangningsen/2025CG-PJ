import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-71))
r=w0.workplane(offset=96/2).moveTo(-4,-41.5).box(8,27,96).union(w0.workplane(offset=126/2).moveTo(-3,-42).cylinder(126,58)).union(w0.workplane(offset=142/2).moveTo(27,29.5).box(68,141,142))