import cadquery as cq
w0=cq.Workplane('YZ',origin=(-47,0,0))
r=w0.sketch().arc((-61,90),(-98,13),(-32,-40)).arc((84,-68),(36,42)).arc((23,70),(-1,90)).close().assemble().reset().face(w0.sketch().arc((-25,8),(-19,18),(-10,26)).arc((-48,42),(-25,8)).assemble(),mode='s').finalize().extrude(84).union(w0.workplane(offset=94/2).moveTo(-31.5,28).box(83,128,94))