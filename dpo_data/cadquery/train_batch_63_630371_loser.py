import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,38))
r=w0.sketch().arc((-13,10),(-38,-12),(-9,-22)).arc((99,13),(-13,10)).assemble().finalize().extrude(-95).union(w0.sketch().push([(-69,-29)]).circle(31).circle(20,mode='s').push([(-4.5,-7.5)]).rect(107,5).finalize().extrude(19))