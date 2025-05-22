import cadquery as cq
w0=cq.Workplane('YZ',origin=(-75,0,0))
w1=cq.Workplane('ZX',origin=(0,-37,0))
r=w0.sketch().arc((-3,27),(-68,-86),(29,0)).arc((75,88),(-3,27)).assemble().finalize().extrude(132).union(w0.workplane(offset=150/2).moveTo(28,-34).cylinder(150,21)).union(w1.sketch().push([(-34,21)]).circle(54).push([(-57,46)]).circle(9,mode='s').push([(-34,21)]).circle(16,mode='s').finalize().extrude(109))