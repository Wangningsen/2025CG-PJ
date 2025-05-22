import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,50))
w1=cq.Workplane('XY',origin=(0,0,31))
r=w0.sketch().push([(-80,-0.5)]).rect(40,23).push([(-80,-0.5)]).rect(12,13,mode='s').finalize().extrude(-100).union(w1.sketch().push([(45,0)]).circle(55).circle(47,mode='s').finalize().extrude(-22))