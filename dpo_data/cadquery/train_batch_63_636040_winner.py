import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,5))
w1=cq.Workplane('XY',origin=(0,0,-5))
r=w0.workplane(offset=-76/2).moveTo(0,24).cylinder(76,37).union(w0.sketch().push([(11,-35)]).circle(17).circle(12,mode='s').push([(87,-48)]).circle(13).finalize().extrude(67)).union(w1.sketch().push([(-65,4)]).circle(35).push([(-56,1)]).circle(20,mode='s').finalize().extrude(44))