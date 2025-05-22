import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().circle(29).reset().face(w0.sketch().segment((-19,4),(6,4)).segment((9,2)).segment((11,4)).segment((13,4)).segment((13,21)).segment((-13,21)).segment((-16,23)).segment((-17,21)).segment((-19,21)).close().assemble(),mode='s').finalize().extrude(-200)