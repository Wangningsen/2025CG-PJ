import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-59))
w1=cq.Workplane('YZ',origin=(-96,0,0))
r=w0.sketch().arc((-23,-24),(-13,-87),(18,-32)).segment((22,-32)).segment((22,-36)).segment((100,-36)).segment((100,-6)).segment((-23,-6)).close().assemble().finalize().extrude(-22).union(w0.sketch().segment((-16,83),(-14,85)).segment((-13,83)).arc((-11,91),(-16,100)).arc((-14,92),(-16,83)).assemble().finalize().extrude(140)).union(w1.workplane(offset=-4/2).moveTo(-1,3.5).box(198,53,4))