import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,21))
w1=cq.Workplane('ZX',origin=(0,-27,0))
r=w0.sketch().segment((-30,-20),(30,-45)).segment((38,-22)).segment((-22,-2)).close().assemble().finalize().extrude(79).union(w1.sketch().segment((-100,-67),(42,-67)).segment((42,51)).arc((-24,38),(-100,67)).close().assemble().push([(-38,30)]).circle(9,mode='s').finalize().extrude(71))