import cadquery as cq
w0=cq.Workplane('YZ',origin=(10,0,0))
r=w0.sketch().arc((13,-100),(13,-4),(96,41)).arc((-81,52),(13,-100)).assemble().finalize().extrude(-21)