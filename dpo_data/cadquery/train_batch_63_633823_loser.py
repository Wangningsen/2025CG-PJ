import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-17))
w1=cq.Workplane('ZX',origin=(0,-57,0))
r=w0.sketch().segment((-82,34),(-60,34)).arc((-33,14),(-5,34)).segment((5,34)).segment((5,-16)).segment((100,-16)).segment((100,55)).segment((5,55)).segment((5,53)).segment((-5,53)).arc((-33,73),(-60,53)).segment((-82,53)).close().assemble().finalize().extrude(99).union(w1.sketch().push([(-29,-48)]).circle(52).circle(27,mode='s').finalize().extrude(-16))