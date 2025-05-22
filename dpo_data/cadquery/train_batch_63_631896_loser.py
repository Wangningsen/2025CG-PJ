import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,52))
w1=cq.Workplane('XY',origin=(0,0,69))
r=w0.sketch().segment((-100,23),(4,-27)).segment((35,36)).segment((-69,87)).close().assemble().finalize().extrude(-121).union(w1.sketch().arc((86,-87),(100,-57),(86,-26)).close().assemble().finalize().extrude(-26))