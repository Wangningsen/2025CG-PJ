import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,55))
r=w0.sketch().push([(-29,-92)]).rect(132,16).push([(4,9)]).circle(91).push([(50,74)]).circle(11,mode='s').finalize().extrude(-110)