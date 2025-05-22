import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-31))
w1=cq.Workplane('ZX',origin=(0,-32,0))
r=w0.sketch().push([(-65,19)]).circle(13).circle(7,mode='s').finalize().extrude(-69).union(w1.sketch().segment((-43,12),(-5,12)).arc((28,-9),(63,8)).segment((62,8)).segment((62,12)).segment((100,12)).segment((100,57)).segment((65,57)).arc((29,78),(-7,57)).segment((-43,57)).close().assemble().push([(29,34)]).circle(26,mode='s').finalize().extrude(21))