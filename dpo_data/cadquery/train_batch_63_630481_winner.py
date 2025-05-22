import cadquery as cq
w0=cq.Workplane('YZ',origin=(-44,0,0))
r=w0.workplane(offset=82/2).moveTo(-34,40).cylinder(82,60).union(w0.sketch().arc((51,-96),(72,-100),(94,-96)).close().assemble().finalize().extrude(88))