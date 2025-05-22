import cadquery as cq
w0=cq.Workplane('YZ',origin=(-9,0,0))
r=w0.sketch().arc((-83,-12),(-87,-50),(-67,-83)).segment((-67,-94)).segment((-49,-94)).arc((-23,-100),(2,-94)).segment((20,-94)).segment((20,-83)).arc((24,-78),(30,-72)).arc((88,-21),(20,16)).segment((20,23)).segment((2,23)).arc((-23,29),(-49,23)).close().assemble().push([(38.5,81)]).rect(43,38).finalize().extrude(19)