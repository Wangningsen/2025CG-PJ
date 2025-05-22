import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,20,0))
w1=cq.Workplane('YZ',origin=(49,0,0))
r=w0.sketch().push([(-61,35.5)]).rect(78,13).reset().face(w0.sketch().arc((31,-5),(90,-38),(55,20)).segment((55,14)).arc((86,-34),(37,-5)).close().assemble()).finalize().extrude(-38).union(w1.workplane(offset=-1/2).moveTo(-10,43).cylinder(1,10))