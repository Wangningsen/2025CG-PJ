import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-38))
w1=cq.Workplane('XY',origin=(0,0,-43))
r=w0.sketch().push([(-85,-1)]).circle(15).push([(-85.5,-1)]).rect(13,20,mode='s').finalize().extrude(2).union(w0.sketch().segment((-77,13),(13,13)).segment((-2,4)).segment((66,-70)).segment((100,-39)).segment((32,34)).segment((18,21)).segment((18,29)).segment((-77,29)).close().assemble().push([(-30,21)]).rect(38,4,mode='s').finalize().extrude(14)).union(w1.workplane(offset=86/2).moveTo(1.5,67).box(15,6,86))