import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-6,0))
r=w0.sketch().segment((-97,52),(-89,52)).segment((-76,52)).segment((-76,69)).arc((-95,47),(-79,71)).segment((-89,71)).segment((-89,61)).segment((-97,61)).close().assemble().finalize().extrude(5).union(w0.sketch().push([(92,-65)]).circle(8).push([(89,-67)]).circle(3,mode='s').finalize().extrude(12))