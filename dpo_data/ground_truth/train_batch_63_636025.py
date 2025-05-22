import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-54,0))
w1=cq.Workplane('YZ',origin=(70,0,0))
r=w0.workplane(offset=-46/2).moveTo(30,-72).box(130,44,46).union(w0.workplane(offset=51/2).moveTo(-38,37).cylinder(51,57)).union(w0.sketch().arc((-77,51),(-73,15),(-43,-5)).segment((-43,-6)).segment((-32,-6)).segment((-32,-5)).arc((4,30),(-20,75)).arc((-56,82),(-77,51)).assemble().finalize().extrude(154)).union(w1.sketch().segment((-58,-34),(-45,-34)).arc((-23,-29),(-31,-51)).segment((-31,-63)).arc((-14,-21),(-58,-34)).assemble().finalize().extrude(8))