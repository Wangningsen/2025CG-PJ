import cadquery as cq
w0=cq.Workplane('YZ',origin=(-25,0,0))
r=w0.sketch().arc((-64,15),(4,-100),(59,22)).arc((-7,100),(-64,15)).assemble().finalize().extrude(51)