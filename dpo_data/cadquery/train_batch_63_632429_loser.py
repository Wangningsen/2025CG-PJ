import cadquery as cq
w0=cq.Workplane('YZ',origin=(35,0,0))
w1=cq.Workplane('YZ',origin=(36,0,0))
r=w0.sketch().arc((-10,77),(-76,49),(-7,27)).segment((75,27)).segment((75,100)).segment((-10,100)).close().assemble().push([(-36.5,56.5)]).rect(29,3,mode='s').finalize().extrude(-88).union(w0.workplane(offset=19/2).moveTo(45.5,-63.5).box(61,73,19)).union(w1.workplane(offset=-5/2).moveTo(-18,50.5).box(20,75,5))