import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,51))
w1=cq.Workplane('XY',origin=(0,0,42))
r=w0.sketch().segment((-100,23),(4,-27)).segment((35,36)).segment((-69,87)).close().assemble().finalize().extrude(-120).union(w1.sketch().arc((86,-87),(100,-57),(86,-27)).close().assemble().finalize().extrude(26))