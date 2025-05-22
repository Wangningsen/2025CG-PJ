import cadquery as cq
w0=cq.Workplane('YZ',origin=(35,0,0))
r=w0.sketch().arc((-10,77),(-76,48),(-7,27)).segment((75,27)).segment((75,100)).segment((-10,100)).close().assemble().push([(-36,56.5)]).rect(28,3,mode='s').finalize().extrude(-89).union(w0.workplane(offset=18/2).moveTo(45.5,-63.5).box(61,73,18))