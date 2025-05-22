import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-16))
r=w0.sketch().push([(-31.5,6.5)]).rect(79,33).reset().face(w0.sketch().segment((18,61),(21,10)).segment((44,11)).segment((42,62)).close().assemble()).push([(52,-57.5)]).rect(38,85).finalize().extrude(-47).union(w0.sketch().push([(-14,66)]).circle(34).push([(-38,72)]).rect(8,18,mode='s').finalize().extrude(79))