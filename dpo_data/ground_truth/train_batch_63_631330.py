import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,41))
r=w0.workplane(offset=-82/2).cylinder(82,100)