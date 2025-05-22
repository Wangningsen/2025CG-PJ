import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-35))
r=w0.sketch().push([(-38,-11)]).circle(33).circle(31,mode='s').finalize().extrude(17).union(w0.sketch().arc((-75,-34),(-53,-98),(0,-59)).arc((-45,-61),(-75,-34)).assemble().push([(63,28)]).circle(20).finalize().extrude(46)).union(w0.workplane(offset=70/2).moveTo(-27,47).cylinder(70,38))