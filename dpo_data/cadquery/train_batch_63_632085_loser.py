import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-91))
r=w0.workplane(offset=182/2).box(200,56,182)