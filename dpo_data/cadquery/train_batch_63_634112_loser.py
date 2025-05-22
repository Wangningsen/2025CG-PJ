import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-52,0))
r=w0.workplane(offset=10/2).moveTo(-10.5,-51).box(9,98,10).union(w0.sketch().segment((-87,38),(-64,27)).segment((-5,27)).segment((-5,-3)).segment((10,-11)).segment((10,-79)).segment((87,-79)).segment((87,56)).segment((35,56)).segment((-56,100)).close().assemble().push([(48,-11)]).circle(35,mode='s').finalize().extrude(103))