import cadquery as cq
w0=cq.Workplane('YZ',origin=(-2,0,0))
w1=cq.Workplane('XY',origin=(0,0,31))
r=w0.sketch().segment((10,-87),(100,-87)).segment((100,15)).segment((15,15)).arc((-99,31),(10,-4)).close().assemble().push([(-70,47)]).circle(4,mode='s').finalize().extrude(48).union(w1.sketch().segment((-20,-36),(-2,-36)).segment((-2,-33)).arc((31,-5),(18,36)).segment((18,34)).segment((14,34)).segment((14,39)).arc((7,42),(-2,45)).segment((-2,49)).segment((-20,49)).segment((-20,42)).arc((-46,6),(-20,-31)).close().assemble().finalize().extrude(56))