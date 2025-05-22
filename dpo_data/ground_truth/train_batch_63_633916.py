import cadquery as cq
w0=cq.Workplane('YZ',origin=(11,0,0))
r=w0.sketch().segment((-30,-35),(42,-35)).segment((42,-18)).segment((100,-18)).segment((100,82)).segment((-13,82)).segment((-13,4)).segment((-30,4)).close().assemble().finalize().extrude(-65).union(w0.sketch().arc((-64,30),(-3,-76),(-55,35)).arc((-85,80),(-64,30)).assemble().finalize().extrude(43))