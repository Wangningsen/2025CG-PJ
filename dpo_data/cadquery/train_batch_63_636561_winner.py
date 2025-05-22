import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,61,0))
r=w0.sketch().segment((-65,-66),(-48,-66)).arc((-6,-84),(35,-66)).segment((38,-66)).segment((38,-100)).segment((65,-100)).segment((65,-2)).segment((52,-2)).segment((52,12)).segment((35,12)).arc((-6,30),(-48,12)).segment((-65,12)).close().assemble().push([(-22,83)]).circle(17).finalize().extrude(-121)