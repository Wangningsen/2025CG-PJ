import cadquery as cq
w0=cq.Workplane('YZ',origin=(35,0,0))
w1=cq.Workplane('YZ',origin=(36,0,0))
r=w0.workplane(offset=19/2).moveTo(45.5,-63.5).box(61,73,19).union(w1.sketch().segment((-74,38),(-73,38)).arc((-42,12),(-6,27)).segment((75,27)).segment((75,100)).segment((-10,100)).segment((-10,77)).arc((-54,85),(-74,41)).close().assemble().push([(-36,56.5)]).rect(28,3,mode='s').finalize().extrude(-89))