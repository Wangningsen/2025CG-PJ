import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-24,0))
r=w0.sketch().segment((-61,-5),(12,-5)).segment((12,100)).segment((-61,100)).segment((-61,42)).arc((-97,28),(-61,16)).close().assemble().push([(-40.5,49)]).rect(9,14,mode='s').push([(49,-51)]).circle(49).push([(69,-60)]).circle(21,mode='s').finalize().extrude(49)