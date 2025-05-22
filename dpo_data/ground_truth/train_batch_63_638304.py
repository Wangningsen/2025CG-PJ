import cadquery as cq
w0=cq.Workplane('YZ',origin=(19,0,0))
w1=cq.Workplane('XY',origin=(0,0,-36))
r=w0.sketch().segment((-37,5),(-9,5)).arc((35,-100),(78,5)).segment((89,5)).segment((89,100)).segment((-37,100)).close().assemble().finalize().extrude(-100).union(w1.workplane(offset=63/2).moveTo(53,-69).cylinder(63,28))