import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().arc((-64,42),(54,-54),(-37,67)).arc((-61,60),(-64,42)).assemble().finalize().extrude(200)