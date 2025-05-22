import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-59))
w1=cq.Workplane('XY',origin=(0,0,-23))
r=w0.sketch().arc((-23,-26),(-14,-87),(21,-36)).segment((100,-36)).segment((100,-6)).segment((-23,-6)).close().assemble().finalize().extrude(-22).union(w0.sketch().arc((-16,83),(-10,91),(-16,100)).segment((-16,97)).arc((-12,91),(-16,85)).close().assemble().finalize().extrude(140)).union(w1.workplane(offset=53/2).moveTo(-98,-1).box(4,198,53))