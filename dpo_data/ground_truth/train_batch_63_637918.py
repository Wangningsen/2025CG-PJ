import cadquery as cq
w0=cq.Workplane('YZ',origin=(60,0,0))
r=w0.sketch().segment((-43,-12),(-41,-12)).segment((-41,36)).arc((-42,36),(-43,37)).close().assemble().finalize().extrude(-121).union(w0.sketch().segment((-100,14),(-18,14)).segment((-18,-47)).segment((16,-47)).segment((16,99)).segment((-100,99)).close().assemble().push([(72,-71)]).circle(28).finalize().extrude(-70))