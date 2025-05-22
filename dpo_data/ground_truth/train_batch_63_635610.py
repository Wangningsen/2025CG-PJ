import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-29))
w1=cq.Workplane('YZ',origin=(50,0,0))
r=w0.sketch().arc((-4,93),(-39,51),(-2,91)).arc((-4,91),(-4,93)).assemble().finalize().extrude(-71).union(w1.sketch().segment((-99,2),(-18,2)).segment((-18,78)).segment((-37,78)).arc((-68,99),(-98,78)).segment((-99,78)).segment((-99,74)).arc((-100,67),(-99,61)).close().assemble().finalize().extrude(-43))