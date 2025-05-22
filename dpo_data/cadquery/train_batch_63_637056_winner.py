import cadquery as cq
w0=cq.Workplane('YZ',origin=(-40,0,0))
r=w0.workplane(offset=37/2).moveTo(-54.5,-3).box(91,14,37).union(w0.sketch().push([(-23,-6)]).circle(2).reset().face(w0.sketch().segment((43,-42),(73,-42)).segment((73,-39)).arc((100,0),(73,39)).segment((73,42)).segment((43,42)).segment((43,39)).arc((16,0),(43,-39)).close().assemble()).finalize().extrude(80))