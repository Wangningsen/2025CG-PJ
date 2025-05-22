import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,61,0))
r=w0.sketch().push([(-40,-44)]).circle(56).reset().face(w0.sketch().segment((36,15),(96,15)).segment((96,66)).segment((52,66)).segment((52,100)).segment((36,100)).segment((36,93)).arc((27,75),(36,55)).close().assemble()).finalize().extrude(-123)