import cadquery as cq
w0=cq.Workplane('YZ',origin=(-27,0,0))
r=w0.workplane(offset=32/2).moveTo(69,-72.5).box(14,55,32).union(w0.sketch().segment((-76,66),(-57,43)).segment((-57,-9)).segment((-48,-9)).arc((41,-25),(-27,34)).segment((-27,51)).arc((-12,68),(-14,90)).arc((-20,83),(-28,78)).segment((-43,78)).arc((-54,87),(-59,100)).arc((-68,87),(-69,71)).close().assemble().finalize().extrude(54))