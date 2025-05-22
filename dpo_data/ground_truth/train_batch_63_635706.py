import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-62,0))
r=w0.sketch().segment((-100,11),(-21,-45)).arc((42,5),(14,-71)).segment((43,-91)).segment((100,-11)).segment((15,50)).segment((3,79)).segment((-15,72)).segment((-43,91)).close().assemble().finalize().extrude(102).union(w0.sketch().push([(10,33)]).circle(30).circle(10,mode='s').finalize().extrude(124))