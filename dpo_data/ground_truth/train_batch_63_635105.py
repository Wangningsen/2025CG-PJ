import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
r=w0.workplane(offset=-8/2).moveTo(-21,0).box(38,108,8).union(w0.sketch().segment((-79,36),(-44,36)).segment((-44,-85)).segment((-31,-100)).segment((79,4)).segment((-11,100)).close().assemble().push([(-21,0)]).circle(3,mode='s').finalize().extrude(35))