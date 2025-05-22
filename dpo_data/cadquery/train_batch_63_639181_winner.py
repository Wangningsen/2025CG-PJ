import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-5))
r=w0.sketch().segment((-100,-44),(-78,-44)).segment((-78,-62)).segment((-49,-62)).segment((-49,-44)).segment((-27,-44)).segment((-27,-14)).segment((-49,-14)).segment((-49,4)).segment((-78,4)).segment((-78,-14)).segment((-100,-14)).close().assemble().finalize().extrude(-69).union(w0.workplane(offset=80/2).moveTo(54,16).cylinder(80,46))