import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-4))
r=w0.sketch().push([(47.5,6)]).rect(35,84).push([(55,21)]).circle(9,mode='s').finalize().extrude(-96).union(w0.sketch().push([(-28,5)]).circle(38).circle(32,mode='s').finalize().extrude(74)).union(w0.workplane(offset=104/2).moveTo(27.5,-4.5).box(77,87,104))