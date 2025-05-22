import cadquery as cq
w0=cq.Workplane('YZ',origin=(58,0,0))
r=w0.sketch().segment((-100,1),(-34,1)).segment((-34,44)).segment((23,44)).segment((23,56)).segment((-100,56)).close().assemble().reset().face(w0.sketch().segment((-43,-56),(100,-56)).segment((100,41)).segment((36,41)).segment((36,-43)).segment((-34,-43)).segment((-34,-13)).segment((-43,-13)).close().assemble()).finalize().extrude(-115)