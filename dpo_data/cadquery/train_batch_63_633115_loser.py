import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,8,0))
w1=cq.Workplane('YZ',origin=(28,0,0))
r=w0.sketch().segment((-97,-61),(3,-61)).segment((3,-13)).arc((8,8),(3,28)).segment((3,77)).segment((-97,77)).segment((-97,28)).arc((-100,8),(-97,-13)).close().assemble().finalize().extrude(-98).union(w1.workplane(offset=-105/2).moveTo(25.5,78.5).box(129,43,105))