import cadquery as cq
w0=cq.Workplane('YZ',origin=(-13,0,0))
w1=cq.Workplane('YZ',origin=(25,0,0))
r=w0.sketch().segment((-49,0),(-44,0)).segment((-44,-1)).segment((-48,-1)).arc((28,51),(-49,0)).assemble().finalize().extrude(-87).union(w1.sketch().arc((58,-79),(63,-74),(58,-68)).close().assemble().finalize().extrude(75))