import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-41))
r=w0.workplane(offset=-59/2).moveTo(3,0).cylinder(59,13).union(w0.sketch().segment((-42,-60),(-31,-62)).arc((14,-74),(57,-51)).segment((58,-49)).segment((58,-50)).arc((64,-43),(69,-35)).segment((72,-28)).arc((56,6),(64,42)).arc((-50,54),(-41,-61)).close().assemble().finalize().extrude(141))