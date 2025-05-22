import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-36))
w1=cq.Workplane('YZ',origin=(-81,0,0))
r=w0.workplane(offset=63/2).moveTo(53,-68).cylinder(63,28).union(w1.sketch().segment((-37,5),(-8,5)).arc((35,-100),(79,5)).segment((90,5)).segment((90,100)).segment((-37,100)).close().assemble().finalize().extrude(100))