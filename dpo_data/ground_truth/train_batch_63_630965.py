import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,12,0))
w1=cq.Workplane('ZX',origin=(0,27,0))
r=w0.sketch().segment((-100,-68),(-41,-68)).segment((-68,-60)).segment((-48,7)).segment((-100,7)).close().assemble().finalize().extrude(-43).union(w0.sketch().segment((35,-50),(80,-50)).segment((80,-27)).arc((99,-2),(95,29)).arc((35,-1),(80,48)).segment((80,68)).segment((35,68)).segment((35,44)).arc((15,9),(35,-27)).close().assemble().finalize().extrude(19)).union(w1.workplane(offset=-28/2).moveTo(-42,-30).cylinder(28,3))