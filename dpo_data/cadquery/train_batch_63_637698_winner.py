import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,57))
r=w0.sketch().segment((-78,-100),(-56,-90)).arc((-23,-12),(53,-39)).segment((78,-27)).segment((78,2)).segment((51,2)).segment((51,100)).segment((-51,100)).segment((-51,2)).segment((-78,2)).close().assemble().finalize().extrude(-114)