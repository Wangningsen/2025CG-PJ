import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().push([(19,0)]).circle(10).circle(4,mode='s').finalize().extrude(145).union(w0.sketch().segment((-29,-36),(-23,-36)).segment((-23,36)).segment((-29,36)).segment((-29,10)).arc((-27,8),(-29,7)).close().assemble().finalize().extrude(200))