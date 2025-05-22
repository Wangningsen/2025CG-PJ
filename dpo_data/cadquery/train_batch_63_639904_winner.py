import cadquery as cq
w0=cq.Workplane('YZ',origin=(18,0,0))
r=w0.sketch().push([(41.5,64)]).rect(63,56).reset().face(w0.sketch().segment((18,44),(23,44)).segment((23,47)).segment((18,46)).close().assemble(),mode='s').push([(43,65)]).circle(17,mode='s').push([(46,39)]).circle(6,mode='s').finalize().extrude(-118).union(w0.workplane(offset=82/2).moveTo(-61,-80).cylinder(82,12))