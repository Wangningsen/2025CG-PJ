import cadquery as cq
w0=cq.Workplane('YZ',origin=(19,0,0))
w1=cq.Workplane('YZ',origin=(11,0,0))
r=w0.sketch().segment((-92,-45),(22,-100)).segment((42,-55)).segment((47,-48)).segment((46,-47)).segment((92,45)).segment((-22,100)).segment((-42,55)).segment((-47,48)).segment((-46,47)).close().assemble().finalize().extrude(-94).union(w0.workplane(offset=-10/2).cylinder(10,50)).union(w1.workplane(offset=64/2).box(18,46,64))