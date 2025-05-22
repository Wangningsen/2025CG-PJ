import cadquery as cq
w0=cq.Workplane('YZ',origin=(-65,0,0))
r=w0.sketch().arc((-58,-44),(-40,-72),(-7,-67)).arc((94,-28),(50,68)).segment((50,71)).segment((44,71)).arc((29,74),(13,71)).segment((9,71)).arc((-90,40),(-58,-44)).assemble().finalize().extrude(13).union(w0.workplane(offset=130/2).moveTo(-26,2).cylinder(130,28))