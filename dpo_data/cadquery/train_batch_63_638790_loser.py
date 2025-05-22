import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,55,0))
r=w0.sketch().segment((-100,-67),(-46,-67)).arc((0,-81),(46,-67)).segment((100,-67)).segment((100,67)).segment((46,67)).arc((0,81),(-46,67)).segment((-100,67)).close().assemble().push([(-72.5,38)]).rect(9,10,mode='s').push([(72.5,-38)]).rect(11,10,mode='s').finalize().extrude(-110)