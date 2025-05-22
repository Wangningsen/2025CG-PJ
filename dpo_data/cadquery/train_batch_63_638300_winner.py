import cadquery as cq
w0=cq.Workplane('YZ',origin=(55,0,0))
r=w0.sketch().push([(54,-33)]).circle(25).push([(44,-29)]).circle(12,mode='s').finalize().extrude(-110).union(w0.sketch().push([(-30,75)]).rect(124,50).push([(55,-33.5)]).rect(74,133).push([(88,-87)]).circle(3,mode='s').finalize().extrude(-29))