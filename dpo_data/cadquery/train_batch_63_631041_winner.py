import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,21))
r=w0.sketch().segment((19,-1),(74,-1)).arc((46,12),(19,-1)).assemble().finalize().extrude(-121).union(w0.sketch().push([(-17,-6)]).circle(56).circle(46,mode='s').finalize().extrude(-74)).union(w0.sketch().push([(-9,7)]).circle(55).circle(18,mode='s').finalize().extrude(79))