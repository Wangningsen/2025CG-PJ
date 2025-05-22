import cadquery as cq
w0=cq.Workplane('YZ',origin=(-80,0,0))
w1=cq.Workplane('YZ',origin=(-82,0,0))
r=w0.sketch().segment((-46,28),(-24,28)).segment((-24,43)).arc((-25,45),(-24,46)).segment((-24,47)).segment((-23,47)).segment((-23,46)).arc((-22,45),(-23,43)).segment((-23,29)).segment((-24,29)).segment((-24,100)).segment((-46,100)).close().assemble().finalize().extrude(104).union(w0.workplane(offset=162/2).moveTo(-34,64).box(52,22,162)).union(w1.sketch().arc((-43,-49),(47,-83),(-1,1)).arc((-13,-29),(-43,-49)).assemble().finalize().extrude(24))