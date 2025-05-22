import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,27))
r=w0.workplane(offset=-53/2).box(106,200,53)