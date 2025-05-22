import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,38))
r=w0.sketch().arc((-13,9),(-38,-13),(-8,-22)).arc((99,13),(-13,9)).assemble().finalize().extrude(-95).union(w0.sketch().push([(-69,-29)]).circle(31).push([(-73,-27)]).circle(22,mode='s').push([(-6.5,-7)]).rect(49,4).finalize().extrude(20))