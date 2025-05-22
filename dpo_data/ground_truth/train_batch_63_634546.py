import cadquery as cq
w0=cq.Workplane('YZ',origin=(-42,0,0))
r=w0.workplane(offset=71/2).moveTo(70.5,-26).box(59,104,71).union(w0.sketch().arc((-28,40),(-84,-40),(-8,21)).segment((8,78)).arc((-18,67),(-28,40)).assemble().reset().face(w0.sketch().arc((6,7),(41,32),(25,73)).close().assemble()).finalize().extrude(84))