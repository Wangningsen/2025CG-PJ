import cadquery as cq
w0=cq.Workplane('YZ',origin=(38,0,0))
w1=cq.Workplane('YZ',origin=(46,0,0))
r=w0.sketch().push([(33,69)]).circle(31).circle(18,mode='s').push([(55,94)]).circle(3,mode='s').finalize().extrude(-97).union(w0.sketch().push([(-85,-80)]).rect(18,36).push([(-82,-90)]).circle(5,mode='s').finalize().extrude(21)).union(w1.workplane(offset=-85/2).moveTo(57,-63).cylinder(85,37))