import cadquery as cq
w0=cq.Workplane('YZ',origin=(46,0,0))
w1=cq.Workplane('XY',origin=(0,0,31))
r=w0.sketch().segment((10,-87),(100,-87)).segment((100,15)).segment((12,15)).arc((-99,31),(10,1)).close().assemble().push([(-71,48)]).circle(5,mode='s').finalize().extrude(-48).union(w1.sketch().segment((-20,-36),(-3,-36)).segment((-3,-33)).arc((33,7),(-3,47)).segment((-3,49)).segment((-20,49)).segment((-20,44)).arc((-46,7),(-20,-31)).close().assemble().finalize().extrude(56))