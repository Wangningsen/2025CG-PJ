import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-3,0))
r=w0.sketch().push([(4,1)]).circle(2).push([(66,14)]).circle(34).push([(49.5,39.5)]).rect(3,5,mode='s').finalize().extrude(-59).union(w0.sketch().push([(-53,-20)]).circle(47).push([(44,64)]).circle(3).reset().face(w0.sketch().segment((43,63),(44,62)).segment((45,65)).segment((44,66)).close().assemble(),mode='s').finalize().extrude(66))