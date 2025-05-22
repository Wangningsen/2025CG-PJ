import cadquery as cq
w0=cq.Workplane('YZ',origin=(-10,0,0))
w1=cq.Workplane('XY',origin=(0,0,61))
r=w0.sketch().push([(-71,-29.5)]).rect(44,43).push([(19,-28)]).circle(33).push([(88,31)]).circle(12).finalize().extrude(-63).union(w0.workplane(offset=-62/2).moveTo(-91,-34).cylinder(62,9)).union(w1.sketch().push([(71,29)]).circle(2).rect(2,2,mode='s').finalize().extrude(-39))