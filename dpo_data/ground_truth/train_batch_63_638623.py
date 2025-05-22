import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,39))
w1=cq.Workplane('XY',origin=(0,0,17))
r=w0.workplane(offset=-78/2).moveTo(78,8).cylinder(78,22).union(w0.sketch().push([(-80.5,-14.5)]).rect(39,65).push([(-83,-37)]).circle(2,mode='s').push([(41,29)]).circle(43).finalize().extrude(-52)).union(w0.sketch().segment((-67,-57),(-64,-72)).segment((-22,-63)).arc((-13,-65),(-6,-60)).segment((35,-51)).segment((32,-36)).segment((-9,-45)).arc((-18,-43),(-25,-48)).close().assemble().finalize().extrude(-50)).union(w1.workplane(offset=-33/2).moveTo(-15.5,-54).box(19,8,33))