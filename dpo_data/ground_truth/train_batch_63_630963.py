import cadquery as cq
w0=cq.Workplane('YZ',origin=(5,0,0))
w1=cq.Workplane('ZX',origin=(0,-42,0))
r=w0.sketch().arc((-86,-75),(-68,-83),(-59,-100)).segment((-14,-100)).segment((-14,10)).segment((-86,10)).segment((-86,8)).arc((-78,-16),(-86,-41)).close().assemble().push([(-83.5,-67.5)]).rect(5,5,mode='s').reset().face(w0.sketch().arc((66,18),(86,59),(66,100)).close().assemble()).finalize().extrude(-43).union(w1.sketch().push([(19.5,0)]).rect(63,102).push([(25,-24)]).circle(14,mode='s').finalize().extrude(54))