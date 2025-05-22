import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,12,0))
w1=cq.Workplane('YZ',origin=(-27,0,0))
r=w0.sketch().segment((-100,-68),(-41,-68)).segment((-68,-60)).segment((-48,7)).segment((-100,7)).close().assemble().finalize().extrude(-43).union(w0.sketch().segment((35,-50),(80,-50)).segment((80,-27)).arc((100,9),(80,45)).segment((80,68)).segment((35,68)).segment((35,45)).arc((15,9),(35,-27)).close().assemble().push([(62,19)]).circle(34,mode='s').finalize().extrude(19)).union(w1.sketch().segment((0,-43),(27,-43)).arc((13,-40),(0,-43)).assemble().finalize().extrude(-6))