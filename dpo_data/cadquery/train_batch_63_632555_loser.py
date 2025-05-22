import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,20,0))
w1=cq.Workplane('ZX',origin=(0,-27,0))
r=w0.sketch().segment((-54,-100),(50,-100)).segment((50,-55)).arc((9,-42),(5,-1)).arc((3,100),(-19,-1)).arc((-22,-5),(-25,-10)).arc((-39,-25),(-54,-41)).close().assemble().finalize().extrude(-19).union(w1.sketch().segment((-30,28),(-10,28)).arc((15,56),(54,69)).arc((52,71),(50,72)).segment((50,76)).segment((44,76)).arc((42,77),(39,76)).segment((34,76)).segment((34,72)).arc((25,68),(18,61)).segment((18,46)).segment((-30,46)).close().assemble().finalize().extrude(54))