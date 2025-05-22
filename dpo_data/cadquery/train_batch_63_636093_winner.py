import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-19))
r=w0.sketch().push([(-25,-48)]).circle(28).push([(1.5,70)]).rect(75,60).push([(2,-13.5)]).rect(44,23).push([(49,-96)]).circle(4).finalize().extrude(-19).union(w0.sketch().push([(2,-13)]).circle(12).push([(10.5,-15)]).rect(7,8,mode='s').finalize().extrude(58))