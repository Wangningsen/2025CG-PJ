import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,35))
w1=cq.Workplane('XY',origin=(0,0,-36))
r=w0.sketch().rect(18,156).reset().face(w0.sketch().segment((-7,26),(-5,26)).segment((-5,24)).segment((0,24)).segment((0,26)).segment((3,26)).segment((3,32)).segment((0,32)).segment((-5,32)).segment((-7,32)).close().assemble(),mode='s').finalize().extrude(-34).union(w1.workplane(offset=71/2).cylinder(71,100))