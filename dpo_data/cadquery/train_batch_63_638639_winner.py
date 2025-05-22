import cadquery as cq
w0=cq.Workplane('YZ',origin=(36,0,0))
w1=cq.Workplane('YZ',origin=(-6,0,0))
r=w0.sketch().arc((-22,2),(20,17),(12,56)).arc((-74,74),(-22,2)).assemble().finalize().extrude(-77).union(w0.sketch().push([(-10,40)]).circle(56).push([(-10.5,40)]).rect(11,8,mode='s').push([(69.5,-88.5)]).rect(23,23).push([(69,-89)]).circle(4,mode='s').finalize().extrude(4)).union(w1.sketch().arc((-62,50),(-58,-10),(-2,-32)).arc((6,-32),(14,-29)).arc((77,-20),(56,34)).arc((3,82),(-62,50)).assemble().finalize().extrude(40))