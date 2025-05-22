import cadquery as cq
w0=cq.Workplane('YZ',origin=(-41,0,0))
w1=cq.Workplane('YZ',origin=(-42,0,0))
r=w0.sketch().segment((-100,-19),(-19,-19)).segment((-19,50)).segment((21,70)).segment((16,78)).segment((-19,60)).segment((-19,61)).segment((-20,61)).segment((-20,62)).segment((-46,55)).segment((-45,52)).segment((-38,54)).segment((-39,42)).segment((-100,42)).close().assemble().reset().face(w0.sketch().segment((-17,0),(22,-78)).segment((100,-40)).segment((55,52)).close().assemble()).finalize().extrude(82).union(w1.workplane(offset=15/2).moveTo(29,-13).cylinder(15,31))