import cadquery as cq
w0=cq.Workplane('YZ',origin=(18,0,0))
r=w0.workplane(offset=-54/2).moveTo(47,0).box(106,114,54).union(w0.sketch().segment((-100,-31),(-42,-31)).segment((-42,17)).arc((-72,17),(-100,36)).close().assemble().push([(-82.5,9.5)]).rect(3,13,mode='s').finalize().extrude(18))