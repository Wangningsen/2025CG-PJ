import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-36))
w1=cq.Workplane('YZ',origin=(19,0,0))
r=w0.workplane(offset=63/2).moveTo(53,-69).cylinder(63,28).union(w1.sketch().segment((-37,12),(-36,12)).segment((-36,5)).segment((-8,5)).arc((35,-100),(78,5)).segment((89,5)).segment((89,12)).segment((90,12)).segment((90,92)).segment((89,92)).segment((89,100)).segment((-36,100)).segment((-36,92)).segment((-37,92)).close().assemble().finalize().extrude(-100))