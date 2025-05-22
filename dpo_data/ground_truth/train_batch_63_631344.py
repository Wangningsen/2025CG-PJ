import cadquery as cq
w0=cq.Workplane('YZ',origin=(-48,0,0))
w1=cq.Workplane('ZX',origin=(0,14,0))
r=w0.workplane(offset=-52/2).moveTo(35,0).cylinder(52,12).union(w0.sketch().arc((9,-43),(37,-50),(64,-41)).segment((64,-21)).segment((80,-21)).arc((68,37),(9,43)).close().assemble().finalize().extrude(-31)).union(w0.workplane(offset=94/2).moveTo(15,-15).box(24,66,94)).union(w1.sketch().arc((-24,7),(-21,8),(-17,9)).segment((-17,100)).segment((-24,100)).close().assemble().push([(-21,88)]).circle(2,mode='s').finalize().extrude(-98))