import cadquery as cq
w0=cq.Workplane('YZ',origin=(10,0,0))
r=w0.sketch().arc((13,-100),(11,-7),(96,41)).arc((-82,50),(13,-100)).assemble().finalize().extrude(-21)