import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-22))
w1=cq.Workplane('YZ',origin=(12,0,0))
r=w0.sketch().segment((-4,0),(3,0)).segment((3,7)).arc((-1,10),(-4,13)).close().assemble().finalize().extrude(84).union(w0.workplane(offset=81/2).moveTo(-98,-28).cylinder(81,1)).union(w1.sketch().segment((-28,-62),(9,-62)).segment((9,-36)).arc((29,-11),(11,13)).segment((11,53)).segment((-14,53)).segment((-14,1)).segment((-28,0)).close().assemble().push([(0,7)]).circle(11,mode='s').finalize().extrude(88))