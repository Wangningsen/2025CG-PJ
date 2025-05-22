import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-3,0))
r=w0.sketch().push([(4,1)]).circle(2).push([(66,14)]).circle(34).reset().face(w0.sketch().segment((46,41),(48,37)).segment((50,37)).segment((48,42)).close().assemble(),mode='s').finalize().extrude(-60).union(w0.sketch().push([(-53,-20)]).circle(47).push([(44.5,64)]).rect(5,6).finalize().extrude(65))