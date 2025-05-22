import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
w1=cq.Workplane('YZ',origin=(-42,0,0))
r=w0.workplane(offset=-3/2).moveTo(-41,-37).cylinder(3,23).union(w0.sketch().segment((44,67),(79,67)).segment((79,91)).segment((79,95)).segment((79,100)).segment((44,100)).close().assemble().push([(73,95)]).circle(3,mode='s').finalize().extrude(48)).union(w1.sketch().segment((-69,-59),(-43,-59)).arc((-9,-79),(25,-59)).segment((51,-59)).segment((51,-23)).segment((25,-23)).arc((-9,-3),(-43,-23)).segment((-69,-23)).close().assemble().finalize().extrude(-58))