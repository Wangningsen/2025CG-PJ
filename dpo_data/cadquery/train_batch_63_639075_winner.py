import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,39))
w1=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().arc((-92,25),(21,-59),(-65,51)).arc((-64,38),(-70,49)).arc((-76,50),(-82,48)).arc((-93,43),(-92,25)).assemble().finalize().extrude(-123).union(w0.workplane(offset=-88/2).moveTo(74,29).cylinder(88,13)).union(w1.workplane(offset=-27/2).moveTo(31,35).cylinder(27,50))