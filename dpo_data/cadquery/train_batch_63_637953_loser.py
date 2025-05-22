import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-18,0))
w1=cq.Workplane('YZ',origin=(48,0,0))
r=w0.sketch().push([(-61,35.5)]).rect(78,13).reset().face(w0.sketch().arc((37,-5),(83,-43),(55,14)).segment((55,19)).arc((92,-36),(37,-5)).assemble()).finalize().extrude(38).union(w1.workplane(offset=1/2).moveTo(-10,43.5).box(20,19,1))