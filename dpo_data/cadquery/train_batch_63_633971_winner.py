import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-65,0))
r=w0.sketch().segment((-67,35),(-25,35)).arc((-17,33),(-9,35)).segment((100,35)).segment((100,95)).segment((-67,95)).close().assemble().finalize().extrude(84).union(w0.sketch().push([(-28,-23)]).circle(72).circle(2,mode='s').finalize().extrude(130))