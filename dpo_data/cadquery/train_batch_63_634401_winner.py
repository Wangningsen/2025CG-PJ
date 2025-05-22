import cadquery as cq
w0=cq.Workplane('YZ',origin=(-2,0,0))
w1=cq.Workplane('XY',origin=(0,0,31))
r=w0.sketch().segment((10,-87),(100,-87)).segment((100,15)).segment((15,15)).arc((-98,35),(10,-3)).close().assemble().push([(-71,45)]).circle(2,mode='s').finalize().extrude(48).union(w1.sketch().segment((-20,-36),(2,-36)).segment((2,-32)).arc((33,7),(2,44)).segment((2,49)).segment((-20,49)).segment((-20,44)).arc((-46,7),(-20,-32)).close().assemble().finalize().extrude(56))