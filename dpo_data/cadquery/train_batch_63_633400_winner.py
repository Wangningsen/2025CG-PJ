import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,88))
w1=cq.Workplane('YZ',origin=(-12,0,0))
r=w0.sketch().arc((-22,41),(21,-41),(23,51)).segment((23,61)).segment((-6,61)).segment((-6,51)).arc((-14,48),(-22,41)).assemble().finalize().extrude(-44).union(w0.workplane(offset=-36/2).moveTo(30,-66).cylinder(36,34)).union(w1.sketch().segment((-32,-88),(100,-88)).segment((100,-1)).segment((63,-1)).arc((50,-3),(37,-1)).segment((-5,-1)).segment((-5,26)).segment((-32,26)).close().assemble().push([(-11,-39)]).circle(20,mode='s').finalize().extrude(-52))