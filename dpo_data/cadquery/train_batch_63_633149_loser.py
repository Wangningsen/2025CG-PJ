import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,14,0))
r=w0.sketch().segment((-70,6),(-48,6)).segment((-49,5)).segment((-45,-5)).segment((-41,-3)).segment((-7,-19)).segment((14,38)).segment((-23,51)).segment((-23,100)).segment((-70,100)).close().assemble().finalize().extrude(-59).union(w0.sketch().push([(27,-71)]).rect(86,58).circle(27,mode='s').finalize().extrude(31))