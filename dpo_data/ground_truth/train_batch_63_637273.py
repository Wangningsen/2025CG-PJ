import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-13,0))
w1=cq.Workplane('YZ',origin=(29,0,0))
r=w0.workplane(offset=-33/2).moveTo(-65,0).cylinder(33,29).union(w1.sketch().segment((-42,52),(-11,52)).segment((-11,22)).arc((-100,-2),(-8,6)).segment((16,6)).segment((16,-53)).segment((100,-53)).segment((100,32)).segment((68,32)).arc((66,48),(57,61)).segment((57,94)).segment((-42,94)).close().assemble().finalize().extrude(-56))