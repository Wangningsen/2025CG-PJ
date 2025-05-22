import cadquery as cq
w0=cq.Workplane('YZ',origin=(-14,0,0))
r=w0.sketch().segment((-2,84),(83,-12)).arc((55,57),(-2,84)).assemble().finalize().extrude(-86).union(w0.workplane(offset=30/2).moveTo(-17,-14).cylinder(30,70)).union(w0.sketch().arc((38,39),(-82,-24),(48,-46)).arc((30,-7),(38,39)).assemble().push([(-13,-11)]).circle(19,mode='s').finalize().extrude(114))