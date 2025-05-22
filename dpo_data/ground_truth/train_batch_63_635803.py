import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
w1=cq.Workplane('XY',origin=(0,0,28))
r=w0.sketch().segment((-23,-69),(-5,-69)).arc((-14,-65),(-23,-69)).assemble().finalize().extrude(-8).union(w1.sketch().arc((-35,53),(-99,-12),(-12,-43)).segment((17,-43)).segment((17,53)).close().assemble().finalize().extrude(41))