import cadquery as cq
w0=cq.Workplane('YZ',origin=(-30,0,0))
r=w0.workplane(offset=-6/2).moveTo(40,-61).cylinder(6,39).union(w0.sketch().segment((23,-89),(57,-89)).arc((40,-29),(23,-89)).assemble().finalize().extrude(33)).union(w0.sketch().arc((-79,54),(-55,33),(-71,5)).segment((13,5)).segment((13,100)).segment((-79,100)).close().assemble().finalize().extrude(66))