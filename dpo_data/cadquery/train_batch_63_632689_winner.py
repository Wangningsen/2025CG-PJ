import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,48))
r=w0.workplane(offset=-96/2).box(200,152,96)