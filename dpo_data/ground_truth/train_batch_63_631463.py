import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-73))
r=w0.sketch().arc((-83,44),(-85,-37),(-5,-43)).arc((99,-24),(9,31)).arc((7,33),(6,35)).segment((6,70)).segment((-83,70)).segment((-83,68)).segment((-73,68)).segment((-73,47)).segment((-83,47)).close().assemble().push([(-38,42)]).circle(21,mode='s').finalize().extrude(147)