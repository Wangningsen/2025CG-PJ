import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-87,-17),(2,-88)).segment((25,-59)).segment((-73,-20)).segment((-61,15)).close().assemble().reset().face(w0.sketch().segment((-25,59),(73,20)).segment((61,-15)).segment((87,17)).segment((-2,88)).close().assemble()).finalize().extrude(-200)