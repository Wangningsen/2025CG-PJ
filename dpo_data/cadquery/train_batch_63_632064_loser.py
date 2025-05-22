import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,20))
w1=cq.Workplane('ZX',origin=(0,-26,0))
r=w0.sketch().segment((-28,-21),(30,-45)).segment((39,-22)).segment((-19,0)).close().assemble().finalize().extrude(80).union(w1.sketch().segment((-100,-67),(42,-67)).segment((42,51)).arc((-29,26),(-100,67)).close().assemble().push([(-38,31)]).circle(6,mode='s').finalize().extrude(70))