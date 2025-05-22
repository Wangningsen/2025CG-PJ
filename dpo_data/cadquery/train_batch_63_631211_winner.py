import cadquery as cq
w0=cq.Workplane('YZ',origin=(-79,0,0))
r=w0.sketch().push([(0,1)]).circle(17).circle(16,mode='s').finalize().extrude(-21).union(w0.sketch().arc((28,8),(-29,-3),(29,2)).arc((25,5),(28,8)).assemble().finalize().extrude(179))