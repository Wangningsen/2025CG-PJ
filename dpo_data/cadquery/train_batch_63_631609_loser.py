import cadquery as cq
w0=cq.Workplane('YZ',origin=(14,0,0))
w1=cq.Workplane('XY',origin=(0,0,9))
r=w0.sketch().push([(67.5,17.5)]).rect(45,45).push([(68,17)]).circle(7,mode='s').finalize().extrude(-89).union(w0.sketch().segment((-35,42),(0,42)).segment((0,22)).arc((-76,4),(1,16)).segment((10,16)).segment((10,100)).segment((-35,100)).close().assemble().finalize().extrude(45)).union(w1.sketch().push([(35,-37)]).circle(40).push([(6,-32)]).circle(6,mode='s').push([(57,-79)]).circle(12).finalize().extrude(-109))