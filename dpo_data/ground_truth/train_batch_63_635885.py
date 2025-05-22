import cadquery as cq
w0=cq.Workplane('YZ',origin=(16,0,0))
w1=cq.Workplane('ZX',origin=(0,-49,0))
r=w0.sketch().segment((3,87),(21,87)).segment((21,99)).segment((6,99)).arc((0,98),(3,93)).close().assemble().push([(3.5,96.5)]).rect(3,5,mode='s').finalize().extrude(66).union(w1.sketch().segment((-100,-12),(-87,-12)).arc((-7,-81),(42,12)).segment((43,12)).segment((43,75)).segment((-40,75)).segment((-40,50)).arc((-71,29),(-87,-5)).segment((-100,-5)).close().assemble().push([(-45,-55)]).circle(9,mode='s').push([(45,-9)]).circle(2,mode='s').finalize().extrude(99))