import cadquery as cq
w0=cq.Workplane('YZ',origin=(4,0,0))
w1=cq.Workplane('ZX',origin=(0,-11,0))
r=w0.workplane(offset=-32/2).moveTo(-29.5,-47.5).box(103,21,32).union(w0.sketch().segment((-80,-2),(-30,-34)).segment((-17,-13)).arc((77,61),(-42,51)).segment((-44,53)).close().assemble().finalize().extrude(-29)).union(w1.sketch().segment((-100,-7),(-65,-7)).arc((-47,-16),(-30,-7)).segment((5,-7)).segment((5,19)).segment((-30,19)).arc((-47,28),(-65,19)).segment((-100,19)).close().assemble().finalize().extrude(-23))