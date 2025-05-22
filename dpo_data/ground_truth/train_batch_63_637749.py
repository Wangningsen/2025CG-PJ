import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-72))
r=w0.workplane(offset=16/2).moveTo(93,-26).cylinder(16,7).union(w0.sketch().arc((-74,40),(-54,-52),(-22,36)).arc((-44,98),(-74,40)).assemble().push([(-70,-22)]).circle(20,mode='s').push([(-8,-80)]).circle(18).finalize().extrude(144))