import cadquery as cq
w0=cq.Workplane('YZ',origin=(17,0,0))
r=w0.workplane(offset=-53/2).moveTo(47,0).box(106,114,53).union(w0.sketch().segment((-100,-31),(-42,-31)).segment((-42,17)).segment((-81,17)).segment((-81,-2)).segment((-96,-2)).segment((-96,19)).segment((-91,19)).segment((-91,35)).segment((-100,35)).close().assemble().finalize().extrude(18))