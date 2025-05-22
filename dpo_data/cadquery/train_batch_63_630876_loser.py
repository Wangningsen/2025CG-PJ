import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-37,0))
r=w0.sketch().push([(-76,25)]).rect(28,150).reset().face(w0.sketch().segment((-86,-13),(-83,-14)).segment((-78,1)).segment((-81,2)).close().assemble(),mode='s').finalize().extrude(4).union(w0.sketch().push([(41,-51)]).circle(49).push([(86.5,-59)]).rect(3,2,mode='s').finalize().extrude(74))