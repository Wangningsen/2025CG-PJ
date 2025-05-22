import cadquery as cq
w0=cq.Workplane('YZ',origin=(-40,0,0))
w1=cq.Workplane('ZX',origin=(0,-9,0))
r=w0.sketch().push([(-23,-5)]).circle(2).reset().face(w0.sketch().segment((43,-42),(73,-42)).segment((73,-39)).arc((100,0),(73,39)).segment((73,42)).segment((43,42)).segment((43,39)).arc((16,0),(43,-39)).close().assemble()).finalize().extrude(80).union(w1.workplane(offset=-91/2).moveTo(-3,-21.5).box(14,37,91))