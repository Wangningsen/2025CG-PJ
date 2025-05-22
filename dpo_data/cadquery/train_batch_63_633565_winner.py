import cadquery as cq
w0=cq.Workplane('YZ',origin=(61,0,0))
r=w0.sketch().arc((-23,9),(-84,-80),(7,-28)).segment((100,-28)).segment((100,96)).segment((-23,96)).close().assemble().reset().face(w0.sketch().segment((-19,24),(28,-21)).segment((95,47)).segment((49,88)).arc((45,89),(42,91)).close().assemble(),mode='s').finalize().extrude(-122)