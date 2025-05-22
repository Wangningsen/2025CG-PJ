import cadquery as cq
w0=cq.Workplane('YZ',origin=(27,0,0))
w1=cq.Workplane('YZ',origin=(-27,0,0))
r=w0.sketch().segment((-99,-12),(-68,-12)).arc((-46,-17),(-24,-12)).segment((-5,-12)).segment((-5,-88)).segment((100,-88)).segment((100,15)).segment((8,15)).segment((8,83)).segment((-24,83)).arc((-46,88),(-68,83)).segment((-99,83)).close().assemble().finalize().extrude(-55).union(w1.sketch().segment((-42,27),(-42,31)).arc((-44,29),(-42,27)).assemble().finalize().extrude(15))