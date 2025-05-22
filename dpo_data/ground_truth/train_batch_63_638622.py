import cadquery as cq
w0=cq.Workplane('YZ',origin=(-41,0,0))
r=w0.sketch().arc((-46,40),(15,-41),(-12,57)).segment((-12,86)).segment((-46,86)).close().assemble().finalize().extrude(-26).union(w0.sketch().segment((-100,1),(-16,-86)).segment((66,-8)).arc((100,20),(59,36)).segment((50,46)).arc((0,27),(-47,52)).close().assemble().finalize().extrude(109))