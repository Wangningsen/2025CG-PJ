import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,94,0))
r=w0.sketch().segment((-58,-93),(45,-100)).segment((58,83)).segment((35,85)).arc((0,100),(-35,89)).segment((-45,90)).close().assemble().reset().face(w0.sketch().arc((-38,24),(0,-47),(38,24)).arc((0,9),(-38,24)).assemble(),mode='s').finalize().extrude(-188)