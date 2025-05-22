import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,37))
r=w0.sketch().segment((-94,-68),(58,-100)).segment((94,68)).segment((-58,100)).close().assemble().reset().face(w0.sketch().segment((-81,-45),(-45,-45)).segment((-45,-44)).arc((-48,-36),(-49,-28)).segment((-81,-28)).close().assemble(),mode='s').finalize().extrude(-74)