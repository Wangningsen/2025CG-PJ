import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-59))
w1=cq.Workplane('ZX',origin=(0,98,0))
r=w0.sketch().arc((-23,-26),(-13,-87),(21,-36)).segment((100,-36)).segment((100,-6)).segment((-23,-6)).close().assemble().finalize().extrude(-22).union(w0.sketch().arc((-16,83),(-10,91),(-16,100)).segment((-16,97)).arc((-12,91),(-16,86)).close().assemble().finalize().extrude(140)).union(w1.workplane(offset=-198/2).moveTo(3.5,-98).box(53,4,198))