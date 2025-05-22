import cadquery as cq
w0=cq.Workplane('YZ',origin=(-15,0,0))
w1=cq.Workplane('YZ',origin=(-16,0,0))
r=w0.sketch().arc((18,-83),(42,-99),(52,-71)).arc((47,-80),(37,-85)).arc((34,-87),(30,-87)).arc((24,-86),(18,-83)).assemble().finalize().extrude(-7).union(w0.sketch().segment((-13,-28),(1,-28)).segment((1,20)).arc((12,35),(1,52)).segment((1,100)).segment((-13,100)).segment((-13,52)).arc((-24,35),(-13,19)).close().assemble().finalize().extrude(36)).union(w1.workplane(offset=39/2).moveTo(-44,-58).box(22,42,39))