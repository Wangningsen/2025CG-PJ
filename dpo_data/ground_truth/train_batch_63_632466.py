import cadquery as cq
w0=cq.Workplane('YZ',origin=(-19,0,0))
r=w0.sketch().arc((-35,94),(-99,-15),(-6,-100)).segment((-11,-95)).segment((-7,-91)).segment((-2,-97)).segment((-5,-100)).arc((99,13),(-31,95)).segment((-31,94)).close().assemble().finalize().extrude(34).union(w0.sketch().arc((-14,-40),(-11,-37),(-10,-41)).arc((12,41),(-14,-40)).assemble().rect(42,36,mode='s').finalize().extrude(38))