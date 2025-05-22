import cadquery as cq
w0=cq.Workplane('YZ',origin=(-5,0,0))
w1=cq.Workplane('YZ',origin=(-19,0,0))
r=w0.sketch().segment((-30,43),(-26,26)).segment((-13,29)).close().assemble().finalize().extrude(-95).union(w0.sketch().segment((-66,40),(-62,29)).segment((62,68)).segment((58,80)).close().assemble().finalize().extrude(105)).union(w1.sketch().arc((16,-80),(34,-52),(66,-49)).arc((32,-50),(16,-80)).assemble().finalize().extrude(10))