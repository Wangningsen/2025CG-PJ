import cadquery as cq
w0=cq.Workplane('YZ',origin=(37,0,0))
r=w0.sketch().arc((-93,25),(-73,-24),(-42,16)).arc((-68,14),(-93,25)).assemble().finalize().extrude(-77).union(w0.sketch().segment((39,12),(99,-19)).segment((100,-17)).segment((40,17)).close().assemble().finalize().extrude(3))