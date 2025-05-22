import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-21))
w1=cq.Workplane('YZ',origin=(12,0,0))
r=w0.sketch().segment((-100,-28),(-99,-29)).segment((-97,-27)).close().assemble().finalize().extrude(80).union(w0.workplane(offset=83/2).moveTo(-2,5).cylinder(83,5)).union(w1.sketch().segment((-28,-62),(9,-62)).segment((9,-38)).segment((11,-38)).segment((11,-35)).arc((29,-12),(11,11)).segment((11,53)).segment((-14,53)).segment((-14,3)).arc((-15,1),(-16,0)).segment((-28,0)).close().assemble().push([(-2,7)]).circle(11,mode='s').finalize().extrude(88))