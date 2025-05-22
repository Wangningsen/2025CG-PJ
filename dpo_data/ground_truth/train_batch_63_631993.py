import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
w1=cq.Workplane('YZ',origin=(-42,0,0))
r=w0.sketch().push([(-41,-48)]).circle(29).circle(17,mode='s').finalize().extrude(-2).union(w0.sketch().push([(61.5,83.5)]).rect(35,33).push([(75,95)]).circle(4,mode='s').finalize().extrude(48)).union(w1.sketch().segment((-69,-59),(-43,-59)).arc((-9,-79),(25,-59)).segment((51,-59)).segment((51,-23)).segment((25,-23)).arc((-9,-3),(-43,-23)).segment((-69,-23)).close().assemble().finalize().extrude(-58))