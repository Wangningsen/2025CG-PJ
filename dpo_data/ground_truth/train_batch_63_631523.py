import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,24))
r=w0.sketch().segment((-100,-6),(-44,-27)).segment((-28,15)).arc((-25,-5),(-16,-23)).arc((24,-98),(69,-25)).arc((81,-3),(83,21)).arc((61,98),(27,26)).segment((10,26)).segment((10,65)).arc((-15,48),(-27,20)).segment((-82,41)).close().assemble().push([(-63,7)]).circle(15,mode='s').finalize().extrude(-48)