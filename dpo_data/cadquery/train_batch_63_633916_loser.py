import cadquery as cq
w0=cq.Workplane('YZ',origin=(11,0,0))
r=w0.sketch().segment((-30,-36),(42,-36)).segment((42,-19)).segment((100,-19)).segment((100,82)).segment((-13,82)).segment((-13,4)).segment((-30,4)).close().assemble().finalize().extrude(-65).union(w0.sketch().arc((-68,29),(-8,-79),(-47,38)).arc((-83,80),(-68,29)).assemble().finalize().extrude(43))