import cadquery as cq
w0=cq.Workplane('YZ',origin=(24,0,0))
w1=cq.Workplane('XY',origin=(0,0,63))
r=w0.sketch().push([(-18,-39)]).circle(25).reset().face(w0.sketch().segment((-33,-43),(-18,-43)).arc((-12,-45),(-8,-43)).segment((-4,-43)).segment((-4,-39)).arc((-2,-39),(-1,-40)).segment((-1,-28)).arc((-8,-27),(-13,-23)).segment((-18,-23)).segment((-18,-33)).segment((-33,-33)).close().assemble(),mode='s').finalize().extrude(76).union(w1.sketch().push([(-58,4)]).rect(84,78).circle(10,mode='s').finalize().extrude(-75))