import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().circle(29).reset().face(w0.sketch().segment((-19,4),(5,4)).arc((9,2),(13,5)).segment((13,21)).segment((-19,21)).close().assemble(),mode='s').finalize().extrude(200)