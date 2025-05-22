import cadquery as cq
w0=cq.Workplane('YZ',origin=(-39,0,0))
w1=cq.Workplane('YZ',origin=(-40,0,0))
r=w0.sketch().push([(-85,-71)]).circle(15).circle(7,mode='s').finalize().extrude(-49).union(w1.sketch().segment((-79,38),(-32,-86)).segment((100,-36)).segment((53,88)).close().assemble().reset().face(w1.sketch().segment((-39,-16),(-19,-16)).segment((-19,-25)).segment((40,-25)).segment((40,-16)).segment((60,-16)).segment((60,18)).segment((40,18)).segment((40,27)).segment((-19,27)).segment((-19,18)).segment((-39,18)).close().assemble(),mode='s').finalize().extrude(128))