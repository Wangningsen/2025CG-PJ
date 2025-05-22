import cadquery as cq
w0=cq.Workplane('YZ',origin=(71,0,0))
r=w0.sketch().circle(100).reset().face(w0.sketch().segment((-98,-22),(-95,-22)).arc((-89,-25),(-82,-22)).segment((-79,-22)).segment((-79,-18)).segment((-82,-18)).arc((-89,-14),(-95,-18)).segment((-98,-18)).close().assemble(),mode='s').push([(-58,-33)]).circle(18,mode='s').finalize().extrude(-142)