import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-11,0))
w1=cq.Workplane('ZX',origin=(0,-38,0))
r=w0.workplane(offset=-25/2).moveTo(0,-23).box(24,16,25).union(w0.sketch().segment((-71,-100),(71,-100)).segment((71,34)).segment((65,32)).segment((65,-90)).segment((-65,-90)).segment((-65,-33)).segment((-70,-35)).segment((-71,-32)).close().assemble().finalize().extrude(-20)).union(w1.sketch().segment((-43,22),(-21,22)).arc((2,15),(26,22)).segment((43,22)).arc((38,25),(34,29)).arc((3,100),(-31,31)).arc((-37,26),(-43,22)).assemble().finalize().extrude(76))