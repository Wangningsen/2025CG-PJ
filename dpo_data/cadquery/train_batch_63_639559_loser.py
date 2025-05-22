import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-38,0))
r=w0.sketch().push([(-49.5,67)]).rect(69,66).reset().face(w0.sketch().arc((-18,1),(-14,-5),(-8,-1)).segment((-2,-1)).segment((-2,9)).segment((-18,9)).close().assemble()).push([(-10,-2)]).circle(2,mode='s').finalize().extrude(14).union(w0.sketch().push([(-58,43)]).circle(1).push([(65,-77)]).rect(38,46).finalize().extrude(76))