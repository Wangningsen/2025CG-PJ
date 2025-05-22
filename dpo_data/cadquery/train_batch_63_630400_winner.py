import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-20))
r=w0.workplane(offset=-19/2).moveTo(-31,-92).cylinder(19,8).union(w0.sketch().segment((-46,12),(-29,10)).arc((-8,1),(16,3)).segment((33,1)).segment((36,16)).arc((49,44),(43,72)).segment((46,87)).segment((29,90)).arc((8,99),(-16,97)).segment((-34,99)).segment((-36,83)).arc((-49,56),(-43,28)).close().assemble().finalize().extrude(59))