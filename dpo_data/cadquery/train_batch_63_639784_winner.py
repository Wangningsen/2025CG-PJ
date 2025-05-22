import cadquery as cq
w0=cq.Workplane('YZ',origin=(45,0,0))
r=w0.sketch().push([(-69,36)]).circle(31).circle(29,mode='s').finalize().extrude(-90).union(w0.sketch().segment((-35,-67),(100,-67)).segment((100,3)).segment((37,3)).arc((-55,36),(-35,-59)).close().assemble().finalize().extrude(-53))