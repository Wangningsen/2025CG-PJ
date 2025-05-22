import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,41,0))
r=w0.sketch().segment((-64,-100),(53,-100)).segment((53,-8)).segment((-3,-8)).segment((-3,25)).arc((-22,25),(-31,43)).segment((-54,43)).segment((-54,-8)).segment((-64,-8)).close().assemble().finalize().extrude(-110).union(w0.sketch().arc((46,91),(19,79),(47,87)).arc((63,95),(46,91)).assemble().finalize().extrude(29))