import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-66,0))
r=w0.workplane(offset=46/2).moveTo(-40.5,-66.5).box(9,45,46).union(w0.workplane(offset=111/2).moveTo(-40.5,-66.5).box(119,25,111)).union(w0.sketch().push([(78,74.5)]).rect(44,29).push([(66,64)]).circle(2,mode='s').push([(78,75)]).circle(7,mode='s').finalize().extrude(132))