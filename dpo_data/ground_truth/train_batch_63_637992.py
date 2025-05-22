import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,34))
r=w0.sketch().push([(-67.5,45)]).rect(39,110).push([(-71.5,0.5)]).rect(13,13,mode='s').push([(52,-54.5)]).rect(70,91).finalize().extrude(-68)