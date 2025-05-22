import cadquery as cq
w0=cq.Workplane('YZ',origin=(18,0,0))
w1=cq.Workplane('YZ',origin=(18,0,0))
r=w0.sketch().segment((-100,-31),(-42,-31)).segment((-42,12)).segment((-46,12)).segment((-46,17)).segment((-91,17)).segment((-91,35)).segment((-100,35)).close().assemble().push([(-97.5,0)]).rect(3,2,mode='s').push([(-94,0)]).rect(4,2,mode='s').finalize().extrude(18).union(w1.workplane(offset=-53/2).moveTo(47,0).box(106,114,53))