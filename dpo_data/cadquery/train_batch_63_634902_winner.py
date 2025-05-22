import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().arc((42,-33),(26,-12),(51,-16)).arc((-46,27),(42,-33)).assemble().finalize().extrude(200)