import cadquery as cq
w0=cq.Workplane('YZ',origin=(-79,0,0))
r=w0.sketch().circle(17).circle(15,mode='s').finalize().extrude(-21).union(w0.sketch().arc((28,7),(-29,-5),(29,2)).arc((25,4),(28,7)).assemble().finalize().extrude(179))