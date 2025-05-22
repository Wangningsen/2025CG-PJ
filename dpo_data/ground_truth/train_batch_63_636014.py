import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,33,0))
w1=cq.Workplane('ZX',origin=(0,54,0))
r=w0.sketch().segment((-92,73),(-88,73)).segment((-72,50)).segment((-46,67)).arc((-43,72),(-39,77)).segment((-40,77)).segment((-56,100)).segment((-89,77)).segment((-92,77)).close().assemble().finalize().extrude(-40).union(w1.sketch().segment((-20,-100),(92,-100)).segment((92,-23)).arc((80,-34),(65,-40)).segment((65,-63)).segment((50,-63)).segment((50,-40)).arc((34,-34),(22,-23)).segment((-20,-23)).close().assemble().finalize().extrude(-109))