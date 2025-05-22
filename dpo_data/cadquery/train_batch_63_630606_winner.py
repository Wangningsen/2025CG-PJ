import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,13))
w1=cq.Workplane('XY',origin=(0,0,15))
r=w0.workplane(offset=-45/2).moveTo(-59,-17).cylinder(45,33).union(w0.sketch().segment((-70,-100),(-66,-100)).segment((-62,-32)).segment((-66,-32)).close().assemble().reset().face(w0.sketch().segment((-28,40),(23,1)).segment((77,64)).segment((24,100)).close().assemble()).finalize().extrude(17)).union(w0.workplane(offset=18/2).moveTo(-21,-13).cylinder(18,39)).union(w1.workplane(offset=17/2).moveTo(49,7).cylinder(17,43))