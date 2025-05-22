import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,0))
r=w0.sketch().push([(28,-10)]).circle(32).circle(29,mode='s').finalize().extrude(-92).union(w0.workplane(offset=-60/2).moveTo(31,-10).cylinder(60,46)).union(w0.sketch().push([(-33,56)]).circle(44).push([(41,-70)]).circle(30).push([(26,-54)]).circle(2,mode='s').finalize().extrude(92))