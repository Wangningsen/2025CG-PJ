import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-18,0))
w1=cq.Workplane('ZX',origin=(0,-20,0))
r=w0.sketch().push([(-61,35.5)]).rect(78,13).reset().face(w0.sketch().arc((30,-9),(92,-36),(55,20)).segment((55,14)).arc((87,-34),(37,-5)).segment((30,-5)).close().assemble()).finalize().extrude(38).union(w1.sketch().push([(42.5,48.5)]).rect(19,1).push([(42.5,49)]).rect(1,2,mode='s').finalize().extrude(20))