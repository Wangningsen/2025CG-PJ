import cadquery as cq
w0=cq.Workplane('YZ',origin=(0,0,0))
w1=cq.Workplane('XY',origin=(0,0,17))
r=w0.sketch().segment((-13,31),(71,31)).segment((71,52)).segment((44,52)).segment((44,66)).segment((-13,66)).close().assemble().push([(28,49)]).circle(3,mode='s').finalize().extrude(-100).union(w0.workplane(offset=100/2).moveTo(-22.5,27.5).box(97,55,100)).union(w1.workplane(offset=-83/2).moveTo(15.5,-22.5).box(95,61,83))