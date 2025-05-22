import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-21))
w1=cq.Workplane('YZ',origin=(12,0,0))
r=w0.workplane(offset=80/2).moveTo(-98,-28).cylinder(80,2).union(w0.workplane(offset=83/2).moveTo(-1,5).cylinder(83,6)).union(w1.sketch().segment((-28,-62),(9,-62)).segment((9,-35)).arc((28,-7),(-3,-4)).segment((-6,-4)).arc((5,-1),(9,8)).segment((11,8)).segment((11,53)).segment((-14,53)).segment((-14,8)).segment((-12,8)).arc((-14,4),(-15,0)).segment((-28,0)).close().assemble().push([(-3,10)]).circle(8,mode='s').finalize().extrude(88))