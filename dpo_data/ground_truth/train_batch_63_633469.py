import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-38))
w1=cq.Workplane('XY',origin=(0,0,-43))
r=w0.sketch().push([(-85,-1)]).circle(15).circle(12,mode='s').finalize().extrude(2).union(w0.sketch().segment((-77,13),(12,13)).segment((-1,2)).segment((66,-70)).segment((100,-39)).segment((33,33)).segment((19,20)).segment((19,29)).segment((-77,29)).close().assemble().push([(-28.5,21.5)]).rect(43,3,mode='s').finalize().extrude(14)).union(w1.workplane(offset=86/2).moveTo(1.5,67).box(15,6,86))