import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-73))
r=w0.sketch().arc((-83,44),(-85,-36),(-8,-45)).arc((98,-28),(8,31)).arc((8,32),(6,33)).segment((6,70)).segment((-83,70)).segment((-83,68)).segment((-73,68)).segment((-73,46)).segment((-83,46)).close().assemble().push([(-37,41)]).circle(21,mode='s').finalize().extrude(146)