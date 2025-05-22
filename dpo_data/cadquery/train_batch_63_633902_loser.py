import cadquery as cq
w0=cq.Workplane('YZ',origin=(31,0,0))
w1=cq.Workplane('YZ',origin=(31,0,0))
r=w0.sketch().segment((-53,-55),(-33,-55)).segment((-33,19)).segment((-53,19)).segment((-53,2)).segment((-53,-17)).close().assemble().reset().face(w0.sketch().arc((34,42),(-11,8),(39,-9)).segment((96,-9)).segment((96,0)).segment((100,0)).segment((100,46)).segment((96,46)).segment((96,55)).segment((34,55)).close().assemble()).finalize().extrude(-63).union(w1.workplane(offset=-49/2).moveTo(-52.5,-9.5).box(95,23,49))