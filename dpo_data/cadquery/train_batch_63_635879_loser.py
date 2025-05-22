import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,9))
r=w0.sketch().segment((-53,-100),(-3,-100)).segment((-3,-47)).segment((53,-47)).segment((53,100)).segment((-34,100)).segment((-34,24)).segment((-53,24)).close().assemble().push([(9,28)]).circle(8,mode='s').finalize().extrude(-65).union(w0.workplane(offset=47/2).moveTo(9.5,16).box(11,28,47))