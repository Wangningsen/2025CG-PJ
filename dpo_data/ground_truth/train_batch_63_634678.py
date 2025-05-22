import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-92))
r=w0.sketch().rect(200,86).reset().face(w0.sketch().segment((66,-30),(78,-36)).segment((84,-24)).segment((72,-18)).close().assemble(),mode='s').finalize().extrude(185)