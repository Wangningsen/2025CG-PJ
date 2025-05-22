import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-88))
r=w0.workplane(offset=176/2).cylinder(176,100)