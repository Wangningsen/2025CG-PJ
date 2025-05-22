import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,12))
r=w0.workplane(offset=-101/2).moveTo(82,-78).cylinder(101,18).union(w0.sketch().segment((-100,-27),(-97,-47)).segment((-2,-34)).segment((-3,-14)).close().assemble().push([(-33,-29)]).circle(3,mode='s').finalize().extrude(-26)).union(w0.workplane(offset=77/2).moveTo(6,74).cylinder(77,22))