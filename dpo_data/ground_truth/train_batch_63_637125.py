import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-52))
r=w0.sketch().push([(-86,-90)]).circle(10).reset().face(w0.sketch().segment((-6,4),(43,-23)).segment((96,73)).segment((47,100)).close().assemble()).finalize().extrude(104)