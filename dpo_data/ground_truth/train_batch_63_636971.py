import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-22))
r=w0.sketch().segment((-45,0),(-33,0)).segment((-33,18)).segment((-32,18)).segment((-32,82)).segment((-33,82)).segment((-33,100)).segment((-45,100)).segment((-45,82)).segment((-45,18)).close().assemble().push([(-39,50)]).circle(3,mode='s').finalize().extrude(9).union(w0.workplane(offset=44/2).moveTo(21,-84.5).box(48,31,44))