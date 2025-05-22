import cadquery as cq
w0=cq.Workplane('YZ',origin=(-94,0,0))
r=w0.sketch().segment((-100,-67),(39,-67)).segment((67,-91)).segment((88,-67)).segment((100,-67)).segment((100,42)).segment((82,42)).arc((29,91),(-20,42)).segment((-41,42)).segment((-69,67)).segment((-91,42)).segment((-100,42)).close().assemble().push([(0,-16)]).circle(25,mode='s').finalize().extrude(188)