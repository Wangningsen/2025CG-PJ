import cadquery as cq
w0=cq.Workplane('YZ',origin=(26,0,0))
r=w0.sketch().push([(-60,90)]).circle(10).push([(52,-82)]).circle(18).push([(52,-82)]).rect(28,10,mode='s').finalize().extrude(-52)