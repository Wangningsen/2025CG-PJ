import cadquery as cq
w0=cq.Workplane('YZ',origin=(11,0,0))
r=w0.sketch().segment((-30,-35),(42,-36)).segment((42,-19)).segment((100,-19)).segment((100,82)).segment((-13,82)).segment((-13,3)).segment((-30,3)).close().assemble().finalize().extrude(-65).union(w0.sketch().arc((-63,29),(-4,-77),(-55,33)).arc((-83,81),(-63,29)).assemble().finalize().extrude(43))