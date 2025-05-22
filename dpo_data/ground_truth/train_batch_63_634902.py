import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().arc((42,-33),(25,-14),(51,-16)).arc((-48,23),(42,-33)).assemble().finalize().extrude(200)