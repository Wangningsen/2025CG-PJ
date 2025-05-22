import cadquery as cq
w0=cq.Workplane('YZ',origin=(-5,0,0))
w1=cq.Workplane('XY',origin=(0,0,-8))
r=w0.workplane(offset=-85/2).moveTo(-84,-36).cylinder(85,16).union(w0.sketch().segment((8,-81),(10,-81)).segment((10,-19)).arc((21,81),(8,-18)).close().assemble().finalize().extrude(31)).union(w0.sketch().push([(87,-60)]).circle(13).circle(8,mode='s').finalize().extrude(96)).union(w1.sketch().segment((-53,30),(-50,30)).segment((-50,28)).segment((24,28)).segment((24,64)).segment((-50,64)).segment((-50,62)).segment((-53,62)).close().assemble().finalize().extrude(-57))