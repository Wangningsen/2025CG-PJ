import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().segment((-58,-4),(57,-13)).segment((58,3)).segment((-58,13)).segment((-58,11)).arc((-55,8),(-55,3)).segment((-53,-2)).close().assemble().finalize().extrude(200)