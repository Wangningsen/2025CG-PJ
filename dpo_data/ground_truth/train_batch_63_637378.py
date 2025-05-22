import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-71,0))
r=w0.sketch().push([(22,-53)]).rect(156,76).circle(15,mode='s').finalize().extrude(16).union(w0.sketch().push([(-66,38)]).rect(68,106).reset().face(w0.sketch().segment((-97,29),(-90,4)).segment((-72,9)).segment((-79,34)).close().assemble(),mode='s').finalize().extrude(143))