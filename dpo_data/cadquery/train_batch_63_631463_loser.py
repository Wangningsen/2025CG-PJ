import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,73))
r=w0.sketch().arc((-83,51),(-81,-40),(3,-47)).arc((99,-24),(16,35)).arc((12,36),(6,37)).segment((6,70)).segment((-83,70)).segment((-83,68)).segment((-69,68)).segment((-69,65)).segment((-83,65)).close().assemble().push([(-38,42)]).circle(21,mode='s').finalize().extrude(-146)