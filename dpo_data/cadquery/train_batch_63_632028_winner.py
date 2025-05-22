import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,7))
w1=cq.Workplane('YZ',origin=(19,0,0))
r=w0.sketch().segment((-19,61),(-15,55)).segment((-7,60)).segment((-12,67)).close().assemble().finalize().extrude(93).union(w1.workplane(offset=-18/2).moveTo(-33,-67).cylinder(18,33))