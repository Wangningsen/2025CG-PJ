import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,57))
r=w0.sketch().arc((-78,-100),(-63,-93),(-53,-81)).arc((-12,-9),(59,-36)).arc((69,-32),(78,-27)).segment((78,2)).segment((51,2)).segment((51,100)).segment((-51,100)).segment((-51,2)).segment((-78,2)).close().assemble().finalize().extrude(-114)